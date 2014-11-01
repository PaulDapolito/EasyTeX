# Project Description and Plan

My project is called EasyTeX, and it is a domain-specific language for quickly creating clean, shareable, and nicely-formatted LaTeX documents. EasyTeX will offer support first for the typesetting of technical problem sets, and will be expanded to support the creation of any technical document.

## Motivation

EasyTex is motivated by a series of external factors as well as LaTeX-specific shortcomings. In more and more areas of Computer Science, we have seen the emergence of transcompiled languages that encompass more popular programming languages by bringing together syntactic sugar and enhanced formatting. These terse languages allow users to produce more quickly and by writing less lines of code, both of which have innumerable benefits in the interests of time and collaboration. 

EasyTeX is motivated by two of such projects. The first is called [Jade](http://jade-lang.com/), which is a template engine for HTML. Jade allows programmers to create HTML pages whose code is clean, easily shareable, and extensible. For example, using the Jade API, the following code transformation is realized when creating a very simple web page:

Jade:

	doctype html
		html(lang="en")
  		head
  			title= Paul's Test Page
  	body
  		h1 Paul's Test Page
  		p.
  			How much less code can we write by using Jade?

Corresponding HTML:

	<!DOCTYPE html>
	<html lang="en">
		<head>
			<title>Paul's Test Page</title>
		</head>
		<body>
			<h1>Paul's Test Page</h1>
		</body>
	</html>

Our code for a simple HTML page is significantly less clunky in Jade, and seems much more human readable. Similar results are yielded using the [CoffeeScript](http://coffeescript.org/) compiler to write a simple Fibonacci function:

CoffeeScript:

	this.fibonnaci = (n) -> 
	    if n == 1 or n == 2 then 1
	    else fibonnaci(n-1) + fibonnaci(n-2)

Corresponding JavaScript:

	this.fibonnaci(n) {
		if (n === 1 || n === 2) {
			return 1;
		} 
		else {
			return fibonnaci(n - 1) + fibonnaci(n - 2);
		}
	}; 

The conciseness and beauty of CoffeeScript are easily realized in this example. By using tools like Jade or CoffeeScript, we are able to develop in powerful languages and do so with code that is easy to write and easy to share. Such is the motivation for EasyTeX. I have often been discouraged from using LaTeX to typeset my work due to the excessive boilerplate markup required to create a document in LaTeX, and the difficulty in maintaining LaTeX documents due to the non-enforcement of styling guidelines in the language. LaTeX documents grow quite quickly, and the language's verbose syntax can make collaboration particularly difficult.


To address these problems, EasyTeX will serve as a domain-specific language to allow for the creation of technical documents more easily and more quickly. When we look at transcompiled languages like Jade and CoffeeScript, we see no loss in functionality when compared with the target language, and we see major gains in the way of productivity, readability, and cleanliness. These are the characteristics that will make EasyTeX useful, as the domain-specific language will encompass lots of LaTeX functionality in a way which is easier for writers to produce. 

It is appropriate for me to create EasyTeX as a domain-specific language because it will be geared more towards technical writings than other areas in which LaTeX is used. In truth, LaTeX can be used to beautifully typeset just about any sort of publication, but EasyTeX will allow for more streamlined typesetting in technical documents, such as memorandums or problem sets. I feel that adhering closely to this domain will allow me to develop EasyTeX more naturally and from a self-serving perspective. As was true in my own experience and what is further confirmed by observation, many students at Harvey Mudd College do not begin typesetting their work until it becomes required in some course (like CS81). While this may be due to personal preference in some cases, I feel that more students would typeset their work if the LaTeX learning curve wasn't so steep, and if the language was easier to access and create documents with. EasyTeX will try to remove this barrier of entry from typesetting technical work. 

## Language Domain

The domain of EasyTeX is technical typesetting. I hope to enable students, professors, scientists, and anyone else who wishes to typeset technical documents and problem sets to do so in the easiest way possible. This domain is useful because of its wide use and application in everyday life: it is an amazing communication medium in many technical and non-technical fields. Anyone who wishes to typeset something, and allow it to be read by others in a way which is pleasing and presentable, will probably consider using LaTeX. 

I envision EasyTeX as being an end-to-end solution to creating beautiful documents via LaTeX for anyone who wishes to typeset their technical work. There are a few DSLs already in existence for creating technical LaTeX documents, although none seem to have high adoption rates nor do most cater to creating a technical document from start to finish. 

## Language Design

EasyTeX will be designed to be efficient, clean, and easy-to-use. Much like documents written using LaTeX, EasyTeX documents will be text files written in any user's favorite text editor. EasyTeX programs, then, are simply text files that follow EasyTeX's grammar and formatting specifications. When the user desires, EasyTeX will provide an interface by which a text file is transcompiled to LaTeX and then compiled into a PDF. This text-to-PDF sequence constitutes the execution of an EasyTeX program, such that an inputted .txt file outputs a .pdf file under the EasyTeX interpreter.  

EasyTeX files will be parsed and internally represented in a hierarchy of Python objects. I intend to create classes which all share at least one common base class in order to structurally model a LaTeX document that might be written to produce a nicely typeset document. EasyTeX parsing will instantiate all different types of these objects, and then loop over respective data members in order to output well-formated LaTeX code. One might imagine how a user could accidentally ascribe incompatible data members to particular elements of the document they wish to produce. Because parsing EasyTeX will create a tree of objects internally, user input will be checked every time a new object in the hierarchy is constructed. This ensures that EasyTeX will be able to produce errors that tell the user exactly where their input was problematic (perhaps by showing the faulty input and what the object being instantiated expects upon initialization). Such real-time error-checking will allow EasyTeX users to easily identify and attempt to rectify syntax, run-time, and compile-time errors.

While error-checking at every level of EasyTeX's internal representation will clearly elucidate errors to users, I insist on designing EasyTeX in order to prevent errors whenever possible. Because EasyTeX serves as a mapping from a cleanly formatted textual syntax to LaTeX, EasyTeX must be thoroughly tested in its ability to output valid LaTeX code. I will design EasyTeX will the intention that, if a user is formatting their EasyTeX document incorrectly, initialization of the various components of EasyTeX's internal representation will derive and clearly explain an error in lieu of outputting invalid lines of LaTeX. This level of detail will require thorough testing of EasyTeX's internal representation and LaTeX output, which, when coupled with a responsive interpretation process, will allow for a preventative and communicative EasyTeX environment.


## Example Computations


