# EasyTeX Final Write-up - Paul Dapolito

## Introduction
EasyTeX is a domain-specific language for creating clean, shareable, and nicely-formatted technical documents using the popular typesetting language, LaTeX. Students, professors, scientists, and other members of the technical world often wish to typeset their documents in the interest of creating beautiful and readable products unbounded by the difficulties of handwriting. The language of choice for domain task is LaTeX, a general-purpose typesetting language used to create beautiful PDF documents. While LaTeX is quite useful for expressing technical work in a stunning medium, the language requires an excess of boilerplate markup to create a document, and maintaining LaTeX documents can be quite difficult due to the non-enforcement of styling guidelines in the language. This, combined with LaTeX's rather verbose syntax, make maintaining and collaborating on technical documents particularly difficult.

EasyTeX serves as a domain-specific language to allow for the creation of technical documents, like memorandums and problem sets, more easily and more quickly with a focus on readability. Collaboration is an important aspect of progress in the technical world, and to complement this paradigm, EasyTeX adheres to strict styling guidelines and formatting specifications to ensure that documents written in the language are shareable. Further than this, EasyTeX encapsulates boilerplate markup and "starter code" to enable users to produce beautiful documents in an efficient manner while still maintaining readability. In the domain of technical typesetting, there is a need for standardization and optimization in the best interests of collaboration and progress, and EasyTeX strives to deliver this typesetting experience in a way that is fast, easy-to-use, and shareable. 

## Language Design

EasyTeX is designed to allow users to express their technical work using their favorite text editor. In developing EasyTeX, I have created sample programs in my favorite text editor, [Sublime Text 2](http://www.sublimetext.com/2). This is simply my own preferred environment for typesetting documents, and EasyTeX users are not restricted to any one editor or environment, as the language's transcompiler will handle any file from any editor, so long as the file consists of text content which matches EasyTeX's [grammar](https://github.com/PaulDapolito/EasyTeX/blob/master/documents/grammar.md) and specifications:

If a user creates an EasyTeX document that meets these criteria and saves it with a `.txt` extension (although no particular file extension is required to use EasyTeX), they can invoke the EasyTeX build process by passing their file to EasyTeX's command-line interface. 

EasyTeX's syntax is designed to be concise and intuitive. The language does not incorporate the notion of opening and closing tags, and instead relies on tabbed-delineation to differentiate between different components of EasyTeX documents. This feature grants EasyTeX users a less verbose syntax than a more general purpose typesetting language, like LaTeX, and encourages readability in users' documents by way of requiring whitespace separation between components. The language's syntax is also meant align closely with a user's expectation as to what should be written. For example, if a user wishes to add certain LaTeX packages to their EasyTeX document in the interest of incorporating more advanced formatting or styling, they can do so by adding some number of comma-separated package names after a `packages:` specifier. This syntax design adheres closely to the English language and will allow users to add and modify components of their documents without having to repeatedly refer to the language's documentation.

When a user creates a text document that meets EasyTeX's specification, they can invoke EasyTeX's build process on the document by passing it to the language's command-line tool. When the EasyTeX tool executes, it takes an input file and attempts to parse it using EasyTeX's [parser](https://github.com/PaulDapolito/EasyTeX/blob/master/source/parser/parser.py). This parser scans the text file for various EasyTeX components (like problems, collaborators, sections, and others) and creates an internal representation of Python objects that holds the inputted text corresponding to reach EasyTeX component. Each object is treated differently by EasyTeX's [interpreter](https://github.com/PaulDapolito/EasyTeX/blob/master/source/interpreters/interpreter.py), and EasyTeX follows an iterative approach to output syntactically correct LaTeX code for each internally represented component of a user's document.

<div style="width: 700px" align="center">
    <img src="./images/computational_model.png"/> <br />
    EasyTeX Computational Model
</div>
&nbsp;
&nbsp;

From EasyTeX's computational model above, we can see that EasyTeX's parser takes a user's input file and creates and internal representation of Python objects. This internal representation takes the form of a hierarchy of objects. At the highest level are the two different types of EasyTeX documents: [`ProblemSet`](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/problem_set.py) and [`Memorandum`](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/memorandums/memorandum.py). These classes each contain data members for each component of an EasyTeX problem set and memorandum, respectively.

An EasyTeX `ProblemSet` consists of an [Author](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/author.py), any number of [Collaborators](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/collaborator.py), an optional [DueDate](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/due_date.py), an optional [Title](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/title.py), an optional [Course](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/course.py), an optional [School](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/school.py), any number of [Packages](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/package.py), and one or more [Problems](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/problem.py). EasyTeX Problems consist of an optional [Label](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/label.py), a [Statement](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/statement.py), and a [Solution](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/solution.py).

<div style="width: 700px" align="center">
    <img src="./images/problem_set.png"/> <br />
    EasyTeX `ProblemSet` (* denotes optional field)
</div>
&nbsp;
&nbsp;

From this schema, an EasyTeX `ProblemSet` takes on the following textual form (with all fields left empty and all optional fields included):

	problem_set:
		author:
		collaborators:
		due_date:
		title:
		course:
		school:
		packages:
		
		problem:
			label:
			statement:
			
			solution:
			
		problem:
			label:
			statement:
				
			solution:

An EasyTeX [Memorandum](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/memorandums/memorandum.py) consists of an [Author](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/author.py), any number of [Collaborators](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/collaborator.py), an optional [Date](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/memorandums/date.py), a [Title](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/title.py), an optional [Subtitle](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/memorandums/subtitle.py), any number of [Packages](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/package.py), and and one or more [Sections](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/memorandums/section.py). EasyTeX sections consist of a [Title](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/title.py) and [Content](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/memorandums/content.py).

<div style="width: 700px" align="center">
    <img src="./images/memorandum.png"/> <br />
    EasyTeX `Memorandum` (* denotes optional field)
</div>
&nbsp;
&nbsp;

From this schema, an EasyTeX Memorandum takes on the following textual form (with all fields left empty and all optional fields included):

	memorandum:
		author:
		collaborators:
		date:
		title:
		subtitle:
		packages: 
		
		section:
			title:
			content:
				
		section:
			title:
			content: 

EasyTeX users can create a `ProblemSet` or `Memorandum` by creating a text file that matches the EasyTeX specification. When the EasyTeX tool executes, their inputted text is parsed into a corresponding internal representation using the hierarchy of objects described above, which is then passed to EasyTeX's interpreter for evaluation. The user can manipulate and re-configure these data by repeatedly invoking EasyTeX's command-line tool on their input file. The control flow of this process is controlled by EasyTeX's parser, internal representation, and interpreter. EasyTeX's parser traverses through each line of the user's text file and attempts to create an internal representation using the aforementioned Python classes. If the user's text file is syntactically valid and can be parsed, then the EasyTeX parser yields an internally represented EasyTeX document which is either a `ProblemSet` or a `Memorandum`. This document is then handed to EasyTeX's interpreter, which produces properly formatted LaTeX code for each component of the internal representation corresponding to a user's EasyTeX document. EasyTeX's interpreter saves this LaTeX code on the user's file system in a `.tex` file, which is outputted in a readable manner to allow the user to refer to the underlying LaTeX of their typeset document. EasyTeX's command-line tool invokes a LaTeX compiler on the `.tex` file to produce `.pdf` file for the user.

<div style="width: 700px" align="center">
	<img src="./images/control_flow.png"/> <br />
    EasyTeX Control Flow
</div>
&nbsp;
&nbsp;

This control flow, from start to finish, is invoked by the user on the command line with an input file:
	
	./easytex.sh input_file_name.txt
	
In order to use EasyTeX, a user must provide an input text file. This file does not need to have a `.txt` extension, but its contents must consist of text that matches the EasyTeX specification. If this inputted text file can be parsed into a valid internal representation, the EasyTeX tool yields a `.tex` file consisting of syntactically correct LaTeX code that corresponds to the user's EasyTeX document. Furthermore, the EasyTeX tool creates a `.pdf` output consisting of the user's typeset  work.

<div style="width: 700px" align="center">
    <img src="./images/input_and_output.png"/> <br />
    EasyTeX Input and Output
</div>
&nbsp;
&nbsp;

There are several cases in which an EasyTeX program could go wrong. Problems with the EasyTeX tool would be encountered when a user inputs a text file that does not meet EasyTeX's specification for valid documents. This might mean that the user omitted a required field or left a field blank, or that the user did not incorporate proper tabbed-delineation as specified by EasyTeX's grammar. Fortunately for the user, however, is that EasyTeX has robust error-checking and outputting functionality. Each class of EasyTeX's internal representation has its own associated error class, meaning that invalid input which is parsed and represented internally produces an error message that tells the user what part of their input was invalid and why it brought about the failure to instantiate EasyTeX's internal representation. EasyTeX's parser also helps users identify and rectify errors in an efficient manner. If, at any point, the EasyTeX parser encounters text that it does not expect and cannot parse, the parser outputs the exact line and column number of the invalid input and what it expected to encounter at that position in the user's document. These error-checking methods provide a standard of exactness when users provide invalid input to EasyTeX. 

While there are not many domain-specific languages on the Internet that target LaTeX directly, LaTeX itself is a domain-specific language for typesetting documents. LaTeX is compiled by a variety of tools, such as `pdflatex`, to create PDF documents. LaTeX can also be compiled to create PostScript documents or DVI documents. There are many such compilers, environments, and tools available for creating LaTeX documents. Many of these tools, such as [TeXworks](http://tug.org/texworks/) and [TeXShop](http://pages.uoregon.edu/koch/texshop/), provide a text-editor (complete with syntax highlighting) environment and allow users to apply a LaTeX compiler to their input. Many LaTeX environments, with a wide array of features, are hosted on the web, such as [writeLaTeX](https://www.writelatex.com/) and [ShareLaTeX](https://www.sharelatex.com/). These environments, upon compilation, produce helpful error messages and highlight lines of input which are invalid in real-time, allowing users to quickly fix their input and reapply the build process for creating typeset documents. While I do strive to create an environment for EasyTeX similar to these interfaces built on web technologies, I have thus far only implemented [syntax highlighting](https://github.com/PaulDapolito/EasyTeX/blob/master/source/EasyTeX%20Grammar.tmLanguage) for the language.

Eventually, I would like to emulate the environment support that surrounds LaTeX. EasyTeX, however, will differ from LaTeX in its formatting standards of cleanliness and simplicity. LaTeX documents often contain a plethora of boilerplate code to specify different facets of a document's format and spacing. I would like to eventually expand EasyTeX to allow users to choose the specific font, margin size, line spacing, and other associated formatting specifications for the documents in a syntactically charming way. However, in the interest of reducing EasyTeX's clunkiness and allowing users, like students at Harvey Mudd, to typeset their work without paying much attention to the tedious setup needed to typeset with LaTeX, EasyTeX currently supports only the explicit specification of LaTeX packages to be included in a user's document with other formatting options, like font style and margin spacing, built-in to the language. 

As was previously mentioned, EasyTeX enforces a whitespace standard of tabbed-delineation to specify the start and end of various components of a user's document. Because LaTeX does not enforce any whitespace standards, the language requires the use of verbose opening and closing tags for all elements of a document. I feel that EasyTeX's enforcement of tabbed-delineation makes EasyTeX documents both more readable and more shareable than LaTeX documents, as EasyTeX users can traverse and identify components of EasyTeX documents more efficiently than they could do so with LaTeX documents. EasyTeX is also very different from LaTeX in terms of the DSL's range of expression. A user can typeset almost any type of document using LaTeX, whether it be a problem set, memorandum, novel, essay, textbook, newspaper, or journal entry. EasyTeX, however, is specific to the domain of typesetting technical problem sets and memorandums. I would certainly like to expand EasyTeX later-on to encompass a wider range of expression, but I feel that focusing on problem sets and memorandums at first has allowed me to produce a high-quality product that is very useful for typesetting these two types of documents. 

## Tutorials by Example

### Problem Sets
Suppose we wanted to typeset a problem set using EasyTeX (assuming all installation and setup for the language as per the project's [README](https://github.com/PaulDapolito/EasyTeX/blob/master/README.md) has been completed). We know, from the specification of a [problem set](https://github.com/PaulDapolito/EasyTeX/blob/master/documents/problem_set.md), the following structure must be maintained to typeset our work:

#### Headers
<table class="tg">
  <tr>
    <th class="tg-e3zv">Field Name</th>
    <th class="tg-e3zv">Required/Optional</th>
  </tr>
  <tr>
    <td class="tg-031e">author</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">collaborators</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">due_date</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">title</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">course</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">school</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">packages</td>
    <td class="tg-031e">Optional</td>
  </tr>
</table>

#### Problems

<table class="tg">
  <tr>
    <th class="tg-e3zv">Field Name</th>
    <th class="tg-e3zv">Required/Optional</th>
  </tr>
  <tr>
    <td class="tg-031e">label</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">statement</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">solution</td>
    <td class="tg-031e">Required</td>
  </tr>
</table>
&nbsp;
&nbsp;

#### Problem Set Example 1

From these specifications, let's create a problem set with one problem and all optional fields filled using our favorite text editor, Sublime Text 2 (the following EasyTeX file is identical to [samples/problem\_set\_sample\_1.txt](https://github.com/PaulDapolito/EasyTeX/blob/master/samples/problem_set_sample_1.txt)):

<div style="width: 700px" align="center">
    <img src="./images/tutorial_1.png"/> <br />
    <code>problem_set_1.txt</code>, EasyTeX File
</div>
&nbsp;
&nbsp;

Now, if we save this file on our Desktop as `problem_set_1.txt`, we can invoke EasyTeX's parser and interpreter on the file by entering EasyTeX's root directory and executing the following command on the command line:

	./easytex.sh ~/Desktop/problem_set_1.txt
	
The command-line interface will print the following two lines to indicate that EasyTeX's computation has completed without errors:

	Running EasyTeX!
	EasyTeX completed computation!

Now, if we look in our Desktop folder, we will see the following four new files:

   * `problem_set_1.pdf`: PDF file corresponding to the inputted EasyTeX file
   * `problem_set_1.tex`: LaTeX file corresponding to the inputted EasyTeX file. This is the `.tex` file that is used to produce the `.pdf` file.
   * `problem_set_1.log`: Log file from the creation of the `.pdf` file.
   * `problem_set_1.aux`: Auxiliary file from the creation of the `.pdf` file.

Two of these files are of much significance. First is the generated LaTeX file, `problem_set_1.tex`. This is the underlying file for the PDF that was produced, and the corresponding LaTeX is outputted as human-readable and nicely formatted code:

<div style="width: 700px" align="center">
    <img src="./images/tutorial_2.png"/> <br />
    <code>problem_set_1.tex</code>, EasyTeX-generated LaTeX File
</div>
&nbsp;
&nbsp;

Second is the generated PDF, `problem_set_1.pdf` representing the typeset version of our EasyTeX problem set:

<div style="width: 700px" align="center">
    <img src="./images/tutorial_3.png" border="1px solid black"/> <br />
    <code>problem_set_1.pdf</code>, EasyTeX-generated PDF
</div>
&nbsp;
&nbsp;

#### Problem Set Example 2

Suppose we wish to create a more lengthy and advanced problem set excluding most of the optional fields. Let's create a problem set with two problems and all optional fields excluded besides the `collaborators` field (the following EasyTeX file is identical to [samples/problem\_set\_sample\_2.txt](https://github.com/PaulDapolito/EasyTeX/blob/master/samples/problem_set_sample_2.txt)):

<div style="width: 700px" align="center">
    <img src="./images/tutorial_4.png"/> <br />
    <code>problem_set_2.txt</code>, EasyTeX File
</div>
&nbsp;
&nbsp;

Invoking EasyTeX using the [easytex.sh](https://github.com/PaulDapolito/EasyTeX/blob/master/easytex.sh) (executing `./easytex.sh ~/Desktop/problem_set_2.txt` from the project's root directory) script yields the following LaTeX and PDF files, respectively:

<div style="width: 700px" align="center">
    <img src="./images/tutorial_5.png"/> <br />
    <code>problem_set_2.tex</code>, EasyTeX-generated LaTeX File
</div>
&nbsp;
&nbsp;

<div style="width: 700px" align="center">
    <img src="./images/tutorial_6.png" border="1px solid black"/> <br />
    <code>problem_set_2.pdf</code>, EasyTeX-generated PDF Page 1
</div>
&nbsp;
&nbsp;

<div style="width: 700px" align="center">
    <img src="./images/tutorial_7.png" border="1px solid black"/> <br />
    <code>problem_set_2.pdf</code>, EasyTeX-generated PDF Page 2
</div>
&nbsp;
&nbsp;

### Memorandums
Suppose we wanted to typeset a memorandum using EasyTeX (assuming all installation and setup for the language as per the project's [README](https://github.com/PaulDapolito/EasyTeX/blob/master/README.md) has been completed). We know, from the specification of a [memorandum](https://github.com/PaulDapolito/EasyTeX/blob/master/documents/memorandum.md), the following structure must be maintained to typeset our work:

#### Headers
<table class="tg">
  <tr>
    <th class="tg-e3zv">Field Name</th>
    <th class="tg-e3zv">Required/Optional</th>
  </tr>
  <tr>
    <td class="tg-031e">author</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">collaborators</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">date</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">title</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">subtitle</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">packages</td>
    <td class="tg-031e">Optional</td>
  </tr>
</table>

#### Sections
<table class="tg">
  <tr>
    <th class="tg-e3zv">Field Name</th>
    <th class="tg-e3zv">Required/Optional</th>
  </tr>
  <tr>
    <td class="tg-031e">title</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">content</td>
    <td class="tg-031e">Required</td>
  </tr>
</table>

#### Memorandum Example 1

From these specifications, let's create a memorandum with one section and all optional fields filled using our favorite text editor, Sublime Text 2 (the following EasyTeX file is identical to [samples/memorandum\_sample\_1.txt](https://github.com/PaulDapolito/EasyTeX/blob/master/samples/memorandum_sample_1.txt)):

<div style="width: 700px" align="center">
    <img src="./images/tutorial_8.png"/> <br />
    <code>memorandum_1.txt</code>, EasyTeX File
</div>
&nbsp;
&nbsp;

Now, if we save this file on our Desktop as `memorandum_1.txt`, we can invoke EasyTeX's parser and interpreter on the file by entering EasyTeX's root directory and executing the following command on the command line:

	./easytex.sh ~/Desktop/memorandum_1.txt
	
The command-line interface will print the following two lines to indicate that EasyTeX's computation has completed without errors:

	Running EasyTeX!
	EasyTeX completed computation!

Now, if we look in our Desktop folder, we will see the following four new files:

   * `memorandum_1.pdf`: PDF file corresponding to the inputted EasyTeX file
   * `memorandum_1.tex`: LaTeX file corresponding to the inputted EasyTeX file. This is the `.tex` file that is used to produce the `.pdf` file.
   * `memorandum_1.log`: Log file from the creation of the `.pdf` file.
   * `memorandum_1.aux`: Auxiliary file from the creation of the `.pdf` file.

Two of these files are of much significance. First is the generated LaTeX file, `memorandum_1.tex`. This is the underlying file for the PDF that was produced, and the corresponding LaTeX is outputted as human-readable and nicely formatted code:

<div style="width: 700px" align="center">
    <img src="./images/tutorial_9.png"/> <br />
    <code>memorandum_1.tex</code>, EasyTeX-generated LaTeX File
</div>
&nbsp;
&nbsp;

Second is the generated PDF, `memorandum_1.pdf` representing the typeset version of our EasyTeX memorandum:

<div style="width: 700px" align="center">
    <img src="./images/tutorial_10.png" border="1px solid black"/> <br />
    <code>memorandum_1.pdf</code>, EasyTeX-generated PDF
</div>
&nbsp;
&nbsp;

#### Memorandum Example 2

Suppose we wish to create a more lengthy and advanced memorandum excluding most of the optional fields. Let's create a memorandum with two sections and all optional fields excluded (the following EasyTeX file is identical to [samples/memorandum\_sample\_2.txt](https://github.com/PaulDapolito/EasyTeX/blob/master/samples/memorandum_sample_2.txt) with some content removed for brevity):

<div style="width: 700px" align="center">
    <img src="./images/tutorial_11.png"/> <br />
    <code>memorandum_2.txt</code>, EasyTeX File
</div>
&nbsp;
&nbsp;

Invoking EasyTeX using the [easytex.sh](https://github.com/PaulDapolito/EasyTeX/blob/master/easytex.sh) (executing `./easytex.sh ~/Desktop/memorandum_2.txt` from the project's root directory) script yields the following LaTeX and PDF files, respectively:

<div style="width: 700px" align="center">
    <img src="./images/tutorial_12.png"/> <br />
    <code>memorandum_2.tex</code>, EasyTeX-generated LaTeX File
</div>
&nbsp;
&nbsp;

<div style="width: 700px" align="center">
    <img src="./images/tutorial_13.png" border="1px solid black"/> <br />
    <code>memorandum_2.pdf</code>, EasyTeX-generated PDF
</div>
&nbsp;
&nbsp;

## Language Implementation

I chose to implement EasyTeX as an external domain-specific language due to my lack of familiarity with languages, other than LaTeX, available for typesetting documents. I have only ever used LaTeX to typeset my work, and my entire motivation in creating EasyTeX was to develop a tool that is less clunky and easier-to-use than LaTeX. EasyTeX has an entirely different syntax and whitespace specification from LaTeX, and I thus decided to implement EasyTeX externally, as I felt that doing so would allow me to truly overcome the shortcomings I have identified in LaTeX.

In creating EasyTeX as an external DSL, I implemented the language entirely in Python. I made this choice because I feel that Python, being a high-level language, enabled to develop quickly and efficiently and try out many different ideas for the project. I have much experience developing software in Python, but I had never implemented a parser in the language before developing EasyTeX's parser. This challenge seemed interesting to me, and I excitedly worked through a robust parser implementation for EasyTeX using Python's [pyparsing](http://pyparsing.wikispaces.com/) module. I also chose to use Python because of the inordinate number of tools and modules available for the language. I have loved developing EasyTeX in the [PyCharm IDE](https://www.jetbrains.com/pycharm/), as it provides great support for executing and reviewing [unit tests](https://docs.python.org/2/library/unittest.html) via the [nose](https://nose.readthedocs.org/en/latest/) module. I wanted to allow myself to focus entirely on designing EasyTeX to meet the goals I specified for the project while avoiding the imposition of any bounds on EasyTeX's expandability, and I felt that Python provided me with the most efficient development experience because of its syntactic simplicity and unbounded [support network](http://stackoverflow.com/questions/tagged/python). In developing EasyTeX, I reaped many of the benefits of choosing Python as its host language, especially while implementing EasyTeX's parser. No matter what problem I came across, I eventually identified a solution by referencing the extensive number of resources available for the language on the Internet.

EasyTeX's software architecture is laid out to be extensible, modular, and hierarchical, all of which were complemented by Python's general-purposeness. I will attempt to describe the language's software architecture along the timeline of the EasyTeX production process. The first major component in allowing an EasyTeX user to typeset their technical documents is the language's build and deploy process. EasyTeX users are able to clone or download the project's repository, which delivers them EasyTeX's source code, tests, documentation, and sample documents. In order to actually use the language, they must then execute the project's [`boostrap.sh`](https://github.com/PaulDapolito/EasyTeX/blob/master/bootstrap.sh) script. This script uses [pip](https://pypi.python.org/pypi/pip), the Python package management tool, to install all of the Python packages required ([pyparsing](http://pyparsing.wikispaces.com/), [coverage](https://pypi.python.org/pypi/coverage), and [nose](https://nose.readthedocs.org/en/latest/)) to use EasyTeX into a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) located on the user's workstation at `/usr/local/EasyTeX/venv`. This bootstrap procedure must be executed only once on a user's machine, and the virtual environment created is invoked each time a user invokes EasyTeX using the project's [`easytex.sh`](https://github.com/PaulDapolito/EasyTeX/blob/master/easytex.sh) script.

<div style="width: 700px" align="center">
    <img src="./images/build_deploy.png"/> <br />
    EasyTeX Build and Deploy Process
</div>
&nbsp;
&nbsp;

This build and deploy procedure is executed every time a commit is added to the project using a [Travis CI repository](https://travis-ci.org/PaulDapolito/EasyTeX). This continuous integration tool clones the repository, performs the bootstrap procedures, and executes EasyTeX's [tests](https://github.com/PaulDapolito/EasyTeX/tree/master/source/tests) each time the project's GitHub repository changes.

When this deployment process is completed once, EasyTeX users are free to create and typeset documents. The first step in this procedure is creating a document in a text editor. While EasyTeX does not yet provide a development environment for users of the language, a [syntax highlighting grammar file](https://github.com/PaulDapolito/EasyTeX/blob/master/source/EasyTeX%20Grammar.tmLanguage) is provided for EasyTeX users to integrate into their text-editing environment. The user can pass their inputted text file to the language's [`easytex.sh`](https://github.com/PaulDapolito/EasyTeX/blob/master/easytex.sh) script on the command line. This script simply activates EasyTeX's virtual environment and passes the user's file to EasyTeX's driver program, [`easytex.py`](https://github.com/PaulDapolito/EasyTeX/blob/master/easytex.py), to begin the EasyTeX compilation and interpretation process.

The first major component of EasyTeX's compilation and interpretation process is the language's [parser](https://github.com/PaulDapolito/EasyTeX/blob/master/source/parser/parser.py). This parser is implemented using Python's [pyparsing](http://pyparsing.wikispaces.com/) module, and as such, EasyTeX's grammar adapted to the specifications of `pyparsing` is included in the parser. The grammar uses a combination of regular expression as well as keyword values from the parsing module. EasyTeX uses this grammar to recursively parse a user's document in its `parse_document` function and instantiate a valid internal representation from a user's document. This functionality is thoroughly tested in the [parser's testing suite](https://github.com/PaulDapolito/EasyTeX/blob/master/source/tests/parser_tests.py), which was implemented using the [unittest](https://docs.python.org/2/library/unittest.html) and [nose](https://nose.readthedocs.org/en/latest/) modules.

If a user's input meets EasyTeX's specifications and yields a valid internal representation, then EasyTeX's parser returns either a [ProblemSet](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/problem_set.py) or a [Memorandum](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/memorandums/memorandum.py). These two classes, which take the form of a hierarchy of Python objects, hold data members for each of the fields that can be included as part of a problem set or memorandum, respectively. Each internal component, implemented using a separate Python class, of an EasyTeX document has its own associated [error class](https://github.com/PaulDapolito/EasyTeX/tree/master/source/errors/ir) to ensure that users are informed when their input does not meet the requirements for a particular class in EasyTeX's internal representation. For example, a user would be notified by EasyTeX's internal `Author` class if they leave the `"author:"` field blank. 

Upon valid instantiation, EasyTeX's parsed internal representation is passed to the language's [interpreter](https://github.com/PaulDapolito/EasyTeX/blob/master/source/interpreters/interpreter.py). This generic interpreter checks if the type of a user's document is a `ProblemSet` or a `Memorandum`, and passes the document to the language's [`problem_set_interpreter`](https://github.com/PaulDapolito/EasyTeX/blob/master/source/interpreters/problem_set_interpreter.py) or [`memorandum_interpreter`](https://github.com/PaulDapolito/EasyTeX/blob/master/source/interpreters/memorandum_interpreter.py), respectively. Each type of document has its own interpreter, which allows some of the same Python classes to be used in both documents while ensuring that the components of each document are interpreted according to the type of the document. Both interpreters are thoroughly tested as part of the language's testing suite for EasyTeX's interpreter, which was implemented using the [unittest](https://docs.python.org/2/library/unittest.html) and [nose](https://nose.readthedocs.org/en/latest/) modules. These interpreters iterate through each object in a document's hierarchical internal representation to produce syntactically-valid and easily-readable LaTeX code. EasyTeX's interpreter creates a LaTeX file in the same directory as the user's input text file. When this `.tex` file is created, EasyTeX's driver program (`easytex.py`) checks to see that the `pdflatex` command is available on the user's machine, and if it is available, executes `pdflatex` on the aforementioned LaTeX file to create a PDF for the user.

<div id="container" style="width: 700px" align="center">
    <img src="./images/architecture_overview.png"/> <br />
    EasyTeX Architecture Overview
</div>

This entire control flow, as highlighted by the diagram above, is facilitated entirely by the `easytex.py` driver program. This driver, when run in the project's virtual environment, creates an instance of the language's parser, opens and reads the user's input text file, and passes it to the parser. If the user's document is parsed correctly, the driver program receives a valid `ProblemSet` or `Memorandum` instance and passes this object to an instance of the language's interpreter to receive a LaTeX (`.tex`) file. The driver program then uses Python's [`sys`](https://docs.python.org/2/library/sys.html), [`os`](https://docs.python.org/2/library/os.html), [`subprocess`](https://docs.python.org/2/library/subprocess.html), [`shlex`](https://docs.python.org/2/library/shlex.html), [`shutil`](https://docs.python.org/2/library/shutil.html), and [`commands`](https://docs.python.org/2/library/commands.html) modules to verify that a user's machine has the `pdflatex` command-line tool and then executes `pdflatex` against the `.tex` file by opening a new process on the user's machine. This production process involved a fair bit of crafty implementation, for EasyTeX must manage and manipulate several files on a user's file system as well as some command-line tools on the user's operating system. 