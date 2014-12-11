# EasyTeX Final Write-up - Paul Dapolito

## Introduction
EasyTeX is a domain-specific language for creating clean, shareable, and nicely-formatted technical documents using the popular typesetting language, LaTeX. Students, professors, scientists, and other members of the technical world often wish to typeset their documents in the interest of creating beautiful and readable products unbounded by the difficulties of handwriting. The language of choice for domain task is LaTeX, a general-purpose typesetting language used to create beautiful PDF documents. While LaTeX is quite useful for expressing technical work in a stunning medium, the language requires an excess of boilerplate markup to create a document, and maintaining LaTeX documents can be quite difficult due to the non-enforcement of styling guidelines in the language. This, combined with LaTeX's rather verbose syntax, make maintaining and collaborating on technical documents particularly difficult.

EasyTeX serves as a domain-specific language to allow for the creation of technical documents, like memorandums and problem sets, more easily and more quickly with a focus on readability. Collaboration is an important aspect of progress in the technical world, and to complement this paradigm, EasyTeX adheres to strict styling guidelines and formatting specifications to ensure that documents written in the language are shareable. Further than this, EasyTeX encapsulates boilerplate markup and "starter code" to enable users to produce beautiful documents in an efficient manner while still maintaining readability. In the domain of technical typesetting, there is a need for standardization and optimization in the best interests of collaboration and progress, and EasyTeX strives to deliver this typesetting experience in a way that is fast, easy-to-use, and shareable. 

## Language Design

EasyTeX is designed to allow users to express their technical work using their favorite text editor. In developing EasyTeX, I have created sample programs in my favorite text editor, [Sublime Text 2](http://www.sublimetext.com/2). This is simply my own preferred environment for typesetting documents, and EasyTeX users are not restricted to any one editor or environment, as the language's transcompiler will handle any file from any editor, so long as the file consists of text content which matches EasyTeX's [grammar](https://github.com/PaulDapolito/EasyTeX/blob/master/documents/grammar.md) and specifications. If a user creates an EasyTeX document and saves it with a `.txt` extension (although no particular file extension is required to use EasyTeX), they can invoke the EasyTeX build process by passing their file to EasyTeX's command-line interface. 

EasyTeX's syntax is designed to be concise and intuitive. The language does not incorporate the notion of opening and closing tags, and instead relies on tabbed-delineation to differentiate between different components of EasyTeX documents. This feature grants EasyTeX users a less verbose syntax than a more general purpose typesetting language, like LaTeX, and encourages readability in users' documents by way of requiring whitespace separation between components. The language's syntax is also meant align closely with a user's expectation as to what should be written. For example, if a user wishes to add certain LaTeX packages to their EasyTeX document in the interest of incorporating more advanced formatting or styling, they can do so by adding some number of comma-separated package names after a `packages:` specifier. This syntax design adheres closely to the English language and will allow users to add and modify components of their documents without having to repeatedly refer to the language's documentation.

When a user creates a text document that meets EasyTeX's specification, they can invoke EasyTeX's build process on the document by passing it to the language's command-line tool. When the EasyTeX tool executes, it takes an input file and attempts to parse it using EasyTeX's [parser](https://github.com/PaulDapolito/EasyTeX/blob/master/source/parser/parser.py). This parser scans the text file for various EasyTeX components (like problems, collaborators, sections, and others) and creates an internal representation of Python objects that holds the inputted text corresponding to reach EasyTeX component. Each object is treated differently by EasyTeX's [interpreter](https://github.com/PaulDapolito/EasyTeX/blob/master/source/interpreters/interpreter.py), and EasyTeX follows an iterative approach to output syntactically correct LaTeX code for each internally represented component of a user's document.

<div style="width: 700px" align="center">
    <img src="./images/computational_model.png"/> <br />
    EasyTeX Computational Model
</div>

From EasyTeX's computational model above, we can see that EasyTeX's parser takes a user's input file and creates and internal representation of Python objects. This internal representation takes the form of a hierarchy of objects. At the highest level is an EasyTeX [Document](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/document.py), which has data fields `problem_set` and `memorandum`. These data members are meant to be populated with objects from EasyTeX's [ProblemSet](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/problem_set.py) and [Memorandum](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/memorandums/memorandum.py) classes, respectively. As one can see in the source code for an EasyTeX Document, a user may specify a document that is either a problem set or a memorandum, but not both. 

An EasyTeX ProblemSet consists of an [Author](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/author.py), any number of [Collaborators](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/collaborator.py), an optional [DueDate](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/due_date.py), an optional [Title](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/title.py), an optional [Course](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/course.py), an optional [School](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/school.py), any number of [Packages](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/shared/package.py), and one or more [Problems](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/problem.py). EasyTeX Problems consist of an optional [Label](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/label.py), a [Statement](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/statement.py), and a [Solution](https://github.com/PaulDapolito/EasyTeX/blob/master/source/ir/problem_sets/solution.py).

<div style="width: 700px" align="center">
    <img src="./images/problem_set.png"/> <br />
    EasyTeX ProblemSet (* denotes optional field)
</div>

From this schema, an EasyTeX ProblemSet takes on the following textual form (with all fields left empty and all optional fields included):

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
    EasyTeX Memorandum (* denotes optional field)
</div>

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

This control flow, from start to finish, is invoked by the user on the command line with an input file:
	
	./easytex.sh input_file_name.txt
	
In order to use EasyTeX, a user must provide an input text file. This file does not need to have a `.txt` extension, but its contents must consist of text that matches the EasyTeX specification. If this inputted text file can be parsed into a valid internal representation, the EasyTeX tool yields a `.tex` file consisting of syntactically correct LaTeX code that corresponds to the user's EasyTeX document. Furthermore, the EasyTeX tool creates a `.pdf` output consisting of the user's typeset  work.

<div style="width: 700px" align="center">
    <img src="./images/input_and_output.png"/> <br />
    EasyTeX Input and Output
</div>

There are several cases in which an EasyTeX program could go wrong. Problems with the EasyTeX tool would be encountered when a user inputs a text file that does not meet EasyTeX's specification for valid documents. This might mean that the user omitted a required field or left a field blank, or that the user did not incorporate proper tabbed-delineation as specified by EasyTeX's grammar. Fortunately for the user, however, is that EasyTeX has robust error-checking and outputting functionality. Each class of EasyTeX's internal representation has its own associated error class, meaning that invalid input which is parsed and represented internally produces an error message that tells the user what part of their input was invalid and why it brought about the failure to instantiate EasyTeX's internal representation. EasyTeX's parser also helps users identify and rectify errors in an efficient manner. If, at any point, the EasyTeX parser encounters text that it does not expect and cannot parse, the parser outputs the exact line and column number of the invalid input and what it expected to encounter at that position in the user's document. These error-checking methods provide a standard of exactness when users provide invalid input to EasyTeX. 

While there are not many domain-specific languages on the Internet that target LaTeX directly, LaTeX itself is a domain-specific language for typesetting documents. LaTeX is compiled by a variety of tools, such as `pdflatex`, to create PDF documents. LaTeX can also be compiled to create PostScript documents or DVI documents. There are many such compilers, environments, and tools available for creating LaTeX documents. Many of these tools, such as [TeXworks](http://tug.org/texworks/) and [TeXShop](http://pages.uoregon.edu/koch/texshop/), provide a text-editor (complete with syntax highlighting) environment and allow users to apply a LaTeX compiler to their input. Many LaTeX environments, with a wide array of features, are hosted on the web, such as [writeLaTeX](https://www.writelatex.com/) and [ShareLaTeX](https://www.sharelatex.com/). These environments, upon compilation, produce helpful error messages and highlight lines of input which are invalid in real-time, allowing users to quickly fix their input and reapply the build process for creating typeset documents. While I do strive to create an environment for EasyTeX similar to these interfaces built on web technologies, I have thus far only implemented [syntax highlighting](https://github.com/PaulDapolito/EasyTeX/blob/master/source/EasyTeX%20Grammar.tmLanguage) for the language.

Eventually, I would like to emulate the environment support that surrounds LaTeX. EasyTeX, however, will differ from LaTeX in its formatting standards of cleanliness and simplicity. LaTeX documents often contain a plethora of boilerplate code to specify different facets of a document's format and spacing. I would like to eventually expand EasyTeX to allow users to choose the specific font, margin size, line spacing, and other associated formatting specifications for the documents in a syntactically charming way. However, in the interest of reducing EasyTeX's clunkiness and allowing users, like students at Harvey Mudd, to typeset their work without paying much attention to the tedious setup needed to typeset with LaTeX, EasyTeX currently supports only the explicit specification of LaTeX packages to be included in a user's document with other formatting options, like font style and margin spacing, built-in to the language. 

As was previously mentioned, EasyTeX enforces a whitespace standard of tabbed-delineation to specify the start and end of various components of a user's document. Because LaTeX does not enforce any whitespace standards, the language requires the use of verbose opening and closing tags for all elements of a document. I feel that EasyTeX's enforcement of tabbed-delineation makes EasyTeX documents both more readable and more shareable than LaTeX documents, as EasyTEX users can traverse and identify components of EasyTeX documents more efficiently than they could do so with LaTeX documents. EasyTeX is also very different from LaTeX in terms of the DSL's range of expression. A user can typeset almost any type of document using LaTeX, whether it be a problem set, memorandum, novel, essay, textbook, newspaper, or journal entry. EasyTeX, however, is specific to the domain of typesetting technical problem sets and memorandums. I would certainly like to expand EasyTeX later-on to encompass a wider range of expression, but I feel that focusing on problem sets and memorandums at first has allowed me to produce a high-quality product that is very useful for typesetting these two types of documents. 