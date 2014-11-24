#!/usr/bin/env python


__author__ = 'Paul Dapolito'

import sys
import os
import subprocess
from commands import getstatusoutput
from parser.parser import EasyTeXParser

from interpreters.interpreter import EasyTeXInterpreter


# Usage: ./easytex.py input_file_name
def main():
    input_file_name = sys.argv[1]

    # Open and read input file
    input_file = open(input_file_name, 'r')
    input_text = input_file.read()

    # Parse input text
    parsed_document = EasyTeXParser().parse_document(input_text)

    # Interpret parsed document
    output_latex_text = EasyTeXInterpreter.interpret_document(parsed_document)

    # Write TeX file
    output_file_name = os.path.splitext(input_file_name)[0] + ".tex"
    output_tex_file = open(output_file_name, "w+")
    output_tex_file.write(output_latex_text)

    # Check for pdflatex, output PDF file if it exists
    # DEVNULL hides output of Popen'd subprocess
    status, result = getstatusoutput("pdflatex -v")
    if status == 0:
        output_directory = os.path.dirname(os.path.relpath(input_file_name))
        bash_command = "pdflatex -output-directory={} {}".format(output_directory, output_file_name)
        DEVNULL = open(os.devnull, 'wb')
        subprocess.Popen(bash_command.split(), stdout=DEVNULL, stderr=subprocess.STDOUT)


if __name__ == "__main__":
    main()