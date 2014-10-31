# Project description and plan

My project is called EasyTeX, and it is a domain-specific language for quickly creating clean, shareable, and nicely-formatted LaTeX documents. EasyTeX will offer support first for the typesetting of technical problem sets, and will be expanded to support the creation of any technical document.

## Motivation

EasyTex is motivated by a series of external factors as well as LaTeX-specific shortcomings. In more and more areas of Computer Science, we have seen the emergence of transcompiled languages which encompass more popular programming languages with high degrees of syntactic sugar and enhanced formatting. These terse languages allow users to produce more quickly and by writing less lines of code, both of which have innumerable benefits in the interests of time and collaboration. 

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

The conciseness and beauty of CoffeeScript are easily realized in this example. By using tools like Jade or CoffeeScript, we are able to develop in powerful languages and do so with code that is easy to write and easy to share. Such is the motivation for EasyTeX. I have often been discouraged from using LaTeX to typeset my work due to the excessive boilerplate markup required to create a document in LaTeX, and the difficulty in maintaining LaTeX documents due to the non-enforcement of styling guidelines  in the language. As was true in my own experience and what is further confirmed by observation, many students at Harvey Mudd do not begin typesetting their work until it becomes required in some course. This may be due to personal preference, but I feel that more students would typeset their work if the LaTeX learning curve wasn't so steep, and if the language was easier to access and create documents with. EasyTeX will try to remove this barrier of entry from typesetting technical work. 

## Language domain

## Language design

## Example computations


