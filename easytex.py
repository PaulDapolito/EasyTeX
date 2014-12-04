__author__ = 'Paul Dapolito'

import sys
import os
import subprocess
import shlex
from commands import getstatusoutput

from source.parser.parser import EasyTeXParser
from source.interpreters.interpreter import EasyTeXInterpreter


# Usage: ./easytex.py input_file_name
def main():
    # Rejoin command-line arguments
    input_file_name = " ".join(sys.argv[1:])

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
    status, result = getstatusoutput("pdflatex -v")
    if status == 0:
        # Point to the correct output directory
        output_directory = os.path.dirname(os.path.realpath(input_file_name))

        # Add hmcpset class file to output directory
        # TODO: Simply copy the file from the include directory using bash
        hmcpset_class = open("source/include/hmcpset.cls").read()
        open(output_directory + "/hmcpset.cls", "w").write(hmcpset_class)

        # Execute bash command, hiding output using DEVNULL
        bash_command = "pdflatex -output-directory='{}' '{}'".format(output_directory, output_file_name)
        split_bash_command = shlex.split(bash_command)
        DEVNULL = open(os.devnull, 'wb')
        subprocess.Popen(split_bash_command, stdout=DEVNULL, stderr=subprocess.STDOUT)


if __name__ == "__main__":
    main()