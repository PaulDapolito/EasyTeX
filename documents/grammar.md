# EasyTeX Grammar

## Overview

EasyTeX's grammar and syntax are divided between its support of memorandums and problem sets. Thus, at the highest level, an EasyTeX document is either a memorandum or a problem set.

An EasyTeX memorandum will consist of a series of textual header fields and then any number of sections for textual content. Memorandum headers will consist of an author, any number of collaborators, a date, a title, and a subtitle. Of these headers, EasyTeX will only require that a user specify a date and a title, with the other header fields being optional. Memorandum sections will consist of a title and content. 

An EasyTeX problem set will consist of a series of textual header fields and then any number of problems. Problem set headers will consist of an author, any number of collaborators, a due date, a title, a class, and a school. The only required headers for an EasyTeX problem set is the author field. A problem within an EasyTeX problem set will consist of an option label, a problem statement, and a solution.

As is supported by EasyTeX's formally stated grammar below, any textual content within an EasyTeX document can be formatted and specified using pre-existing LaTeX markup. In creating the grammar for EasyTeX in Extended Backus-Naur Form, I consulted the notation's [Wikipedia page](http://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_Form).

## EasyTeX Grammar in Extended Backus-Naur Form

	document = memorandum | problem_set ;

	memorandum = "memorandum:", return, tab, author, [collaborators], [date], title, [subtitle], {section} ;
	problem_set = "problem_set:", return, tab, author, [collaborators], [due_date], [title], [course], [school], {problem} ;

	author = "author:", space, text ;
	collaborators = "collaborators:", space, {collaborator} ;
	collaborator = text ;
	date = "date:", space, text ;
	title = "title:", space, text ; 
	subtitle = "subtitle:", space, text ;

	section = "section:", return, tab, title, content ;
	content = "content:", return, tab, text ;
	text = {character} ;

	due_date = "due_date:", space, text ;
	course = "course:", space, text ;
	school = "school:", space, text ;

	problem = "problem:", return, tab, [label], statement, solution ;
	label = "label:", space, {character} ;
	statement = "statement:", space, {character} ;
	solution = "solution:", return, tab, {character} ;

	text = {character} ;
	character = letter | digit | symbol | whitespace ;
	letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
	       		 | "H" | "I" | "J" | "K" | "L" | "M" 
	       		 | "N" | "O" | "P" | "Q" | "R" | "S" 
	       		 | "T" | "U" | "V" | "W" | "X" | "Y" 
	       		 | "Z" | "a" | "b" | "c" | "d" | "e"
	       		 | "f" | "g" | "h" | "i" | "j" | "k"
	       		 | "l" | "m" | "n" | "o" | "p" | "q"
	       		 | "r" | "s" | "t" | "u" | "v" | "w"
	       		 | "x" | "y" | "z" ;
	digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
	symbol = "[" | "]" | "{" | "}" | "(" | ")" | "<" | ">"
	       		 | "'" | '"' | "=" | "|" | "." | "," | ";" 
	       		 | "\" | "/" ;
	whitespace = space | tab | return ;
	space = " " ;
	tab = "\t" ;
	return = "\n" ;
