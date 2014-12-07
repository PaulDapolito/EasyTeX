# EasyTeX
[![Build Status](https://travis-ci.org/PaulDapolito/EasyTeX.svg?branch=master)](https://travis-ci.org/PaulDapolito/EasyTeX)

EasyTeX is a domain-specific language for quickly creating clean, shareable, and nicely-formatted technical documents using LaTeX. EasyTeX will offer support first for the typesetting of technical problem sets and memorandums, and will be expanded later-on to support the creation of any document.

## Dependencies

+ pdflatex (if you want to produce `.pdf` files from input)
+ Python 2.7.x
+ pip

### pdflatex

EasyTeX relies on the `pdflatex` command-line tool in order to create PDF documents from LaTeX files. This command-line tool is included in several [LaTeX packages](http://latex-project.org/ftp.html), such as [MiKTeX](http://miktex.org/download), [MacTeX](http://www.tug.org/mactex/), [TeX Live](http://www.tug.org/texlive/), and [proTeXt](http://www.tug.org/protext/). Please ensure that the `pdflatex` command-line tool is available before attempting to use EasyTeX. If you choose to forgo the installation of a LaTeX package that includes `pdflatex`, EasyTeX will simply output a `.tex` file for properly formatted input.

### Python

Use of EasyTeX relies on [Python](https://www.python.org/) 2.7.x. If your machine does not already have Python installed, you can [download it](https://www.python.org/downloads/) from the web.

### pip

EasyTeX makes use of a wide variety of Python modules. In order to use these modules, you must have 
[pip](https://pypi.python.org/pypi/pip) installed. pip is a Python package manager, and EasyTeX's bootstrap script uses the module to ensure that all proper dependencies are installed for EasyTeX usage.

#### Installing pip

1. Download the [get-pip.py](https://bootstrap.pypa.io/get-pip.py) file.
2. Execute the following command (may require use of `sudo`): `python get-pip.py`

## Installing EasyTeX

1. Clone the repository using `git`:

	`git clone https://github.com/PaulDapolito/EasyTeX.git`

2. In the root directory of the project, run the `bootstrap.sh` script (may require use of `sudo`):

	`./bootstrap.sh`

## Usage Instructions

EasyTeX includes a shell script to allow you to use the tool for end-to-end PDF generation. EasyTeX currently supports two types of documents: [problem sets](https://github.com/PaulDapolito/EasyTeX/blob/master/documents/problem_set.md) and [memorandums](https://github.com/PaulDapolito/EasyTeX/blob/master/documents/problem_set.md). Some samples of these different EasyTeX documents are included in the project's [samples](https://github.com/PaulDapolito/EasyTeX/tree/master/samples) directory.

If you have a file that meets EasyTeX's specifications (as per the language's [grammar](https://github.com/PaulDapolito/EasyTeX/blob/master/documents/grammar.md)), you can generate a PDF for your file by executing: 

	./easytex.sh file_name 
	
This will create PDF and LaTeX files (or only a LaTeX file if `pdflatex` is not installed) in the same directory as the input file. Happy typesetting!

## Sample Usage

Suppose we would like to create a PDF file from a sample EasyTeX file included in [`samples/`](https://github.com/PaulDapolito/EasyTeX/tree/master/samples). To begin this process, we must first download or clone this GitHub repository:

	git clone https://github.com/PaulDapolito/EasyTeX.git

Be sure that your system satisfies the dependencies described above, and enter the root directory for the EasyTeX project. In a `bash` shell, run EasyTeX's `bootstrap.sh` script:
	
	./bootstrap.sh

Now, to create `.pdf` and `.tex` files corresponding to the sample EasyTeX file `samples/memorandum_sample_1.txt`, execute the following command:
	
	./easytex.sh samples/memorandum_sample_1.txt

When this process completes, we will see 4 new files in the `samples` directory:
	
1. `memorandum_sample_1.pdf`: `.pdf` file corresponding to the inputted EasyTeX file.
2. `memorandum_sample_1.tex`: `.tex` file corresponding to the inputted EasyTeX file. This is the `.tex` file that is used to produce the `.pdf` file.
3. `memorandum_sample_1.log`: `.log` file from the creation of the `.pdf` file.
4. `memorandum_sample_1.aux`: `.aux` file from the creation of the `.pdf` file.

For more information on the two particular types of EasyTeX documents, please refer to the pages specific to [problem sets](https://github.com/PaulDapolito/EasyTeX/blob/master/documents/problem_set.md) and [memorandums](https://github.com/PaulDapolito/EasyTeX/blob/master/documents/problem_set.md)!


