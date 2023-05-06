#!/usr/bin/python3

"""
Converts a markdown file to HTML format.

Usage: ./markdown2html.py input.md output.html
"""

import sys
import os
import markdown


def convert_md_to_html(input_file, output_file):
    """
    Converts markdown content from input_file to HTML
    format and writes it to output_file.
    """
    with open(input_file, 'r') as f:
        text = f.read()

    with open(output_file, 'w') as f:
        # convert markdown to html
        html = markdown.markdown(text)

        # write html to output file
        f.write(html)


if __name__ == "__main__":
    # check if correct number of arguments are passed
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py input.md output.html\n")
        sys.exit(1)

    # get input and output filenames
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # check if input file exists
    if not os.path.exists(input_file):
        sys.stderr.write("Missing {}\n".format(input_file))
        sys.exit(1)

    # convert markdown to html and write to output file
    convert_md_to_html(input_file, output_file)

    # exit with success code
    sys.exit(0)
