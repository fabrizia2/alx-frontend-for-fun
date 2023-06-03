#!/usr/bin/python3

"""
Markdown script using python.
"""

import sys
import os.path
import re
import hashlib


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1]) as f_in, open(sys.argv[2], 'w') as f_out:
        unordered_start, ordered_start, paragraph = False, False, False
        for line in f_in:
            line = line.replace('**', '<b>', 1)
            line = line.replace('**', '</b>', 1)
            line = line.replace('__', '<em>', 1)
            line = line.replace('__', '</em>', 1)

            md5 = re.findall(r'\[\[.+?\]\]', line)
            md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
            if md5:
                line = line.replace(md5[0], hashlib.md5(md5_inside[0].encode()).hexdigest())

            remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
            remove_c_more = re.findall(r'\(\((.+?)\)\)', line)
            if remove_letter_c:
                remove_c_more = ''.join(c for c in remove_c_more[0] if c not in 'Cc')
                line = line.replace(remove_letter_c[0], remove_c_more)

            length = len(line)
            headings = line.lstrip('#')
            heading_num = length - len(headings)
            unordered = line.lstrip('-')
            unordered_num = length - len(unordered)
            ordered = line.lstrip('*')
            ordered_num = length - len(ordered)

            if 1 <= heading_num <= 6:
                line = f'<h{heading_num}>' + headings.strip() + f'</h{heading_num}>\n'

            if unordered_num:
                if not unordered_start:
                    f_out.write('<ul>\n')
                    unordered_start = True
                line = '<li>' + unordered.strip() + '</li>\n'
            if unordered_start and not unordered_num:
                f_out.write('</ul>\n')
                unordered_start = False

            if ordered_num:
                if not ordered_start:
                    f_out.write('<ol>\n')
                    ordered_start = True
                line = '<li>' + ordered.strip() + '</li>\n'
            if ordered_start and not ordered_num:
                f_out.write('</ol>\n')
                ordered_start = False

            if not (heading_num or unordered_start or ordered_start):
                if not paragraph and length > 1:
                    f_out.write('<p>\n')
                    paragraph = True
                elif length > 1:
                    f_out.write('<br/>\n')
                elif paragraph:
                    f_out.write('</p>\n')
                    paragraph = False

            if length > 1:
                f_out.write(line)

        if unordered_start:
            f_out.write('</ul>\n')
        if ordered_start:
            f_out.write('</ol>\n')
        if paragraph:
            f_out.write('</p>\n')
    sys.exit(0)
