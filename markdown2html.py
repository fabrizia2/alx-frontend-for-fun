#!/usr/bin/python3

import sys
import os
import markdown

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

# open input and output files
with open(input_file, 'r') as f:
    text = f.read()

with open(output_file, 'w') as f:
    # convert markdown to html
    html = markdown.markdown(text)

    # write html to output file
    f.write(html)

# exit with success code
sys.exit(0)
