__author__ = 'Paul Dapolito'

import sys
import os
import subprocess
import shlex
import shutil
import time
from multiprocessing import Process
from commands import getstatusoutput

from source.parser.parser import EasyTeXParser
from source.interpreters.interpreter import EasyTeXInterpreter


# PD 1/11/2015 - TODO: Do not let this poll forever
def open_pdf(file_name):
    print "Opening PDF"
    while not os.path.exists(file_name):
        time.sleep(1)

    os.system("open '{}'".format(file_name))
    return


# Usage: python easytex.py input_file_name
def main():
    # Rejoin command-line arguments
    input_file_name = " ".join(sys.argv[1:])

    # Open and read input file
    input_file = open(input_file_name, 'r')
    input_text = input_file.read()

    # Parse input text
    print "Parsing input file."
    parsed_document = EasyTeXParser().parse_document(input_text)

    # Interpret parsed document
    print "Interpreting input file."
    output_latex_text = EasyTeXInterpreter.interpret_document(parsed_document)

    # Strip extension from input file name
    stripped_file_name = os.path.splitext(input_file_name)[0]

    # Write TeX file
    print "Writing LaTeX (.tex) file."
    output_file_name = stripped_file_name + ".tex"
    output_tex_file = open(output_file_name, "w+")
    output_tex_file.write(output_latex_text)

    # Check for pdflatex, output and open PDF file if it exists
    print "Attempting to generate PDF."
    sys.path.append("/usr/texbin")
    status, result = getstatusoutput("pdflatex -v")
    if status == 0:
        # Point to the correct output directory
        output_directory = os.path.dirname(os.path.realpath(input_file_name))

        # Add hmcpset class file to output directory
        hmcpset_path = "source/include/hmcpset.cls"
        shutil.copy(hmcpset_path, output_directory)

        # Execute bash command, hiding output using DEVNULL
        print "Executing pdflatex."
        bash_command = "pdflatex -output-directory='{}' '{}'".format(output_directory, output_file_name)
        split_bash_command = shlex.split(bash_command)
        DEVNULL = open(os.devnull, 'wb')
        subprocess.Popen(split_bash_command, stdout=DEVNULL)

        # Open PDF File
        pdf_file_name = stripped_file_name + ".pdf"
        open_pdf_thread = Process(target=open_pdf, args=(pdf_file_name,))
        open_pdf_thread.start()

    else:
        print "Could not generate PDF! Please check that the pdflatex command-line tool is installed."

if __name__ == "__main__":
    main()