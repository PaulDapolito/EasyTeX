# EasyTeX Grammar

## Overview

EasyTeX's grammar and syntax are divided between its support of memorandums and problem sets. Thus, at the highest level, an EasyTeX document is either a memorandum or a problem set.

An EasyTeX memorandum will consist of a series of optional and arbitrarily orderable header fields and then any number of sections for textual content. Memorandum headers will consist of an author, any number of collaborators, a date, a title, and a subtitle. Of these headers, EasyTeX will only require that a user specify a date and a title, with the other header fields being optional. Memorandum sections will consist of a title and content. 

An EasyTeX problem set will consist of a series of optional and arbitrarily orderable header fields and then any number of problems. Problem set headers will consist of an author, any number of collaborators, a due date, a title, a class, and a school. The only required headers for an EasyTeX problem set is the author field. A problem within an EasyTeX problem set will consist of an option label, a problem statement, and a solution.

As is supported by EasyTeX's formally stated grammar below, any textual content within an EasyTeX document can be fulfilled and specified using pre-existing LaTeX markup. In creating the grammar for EasyTeX in Extended Backus-Naur Form, I consulted the notation's [Wikipedia page](http://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_Form).

## EasyTeX Grammar in Extended Backus-Naur Form

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
	number = {digit} ;
	symbol = "[" | "]" | "{" | "}" | "(" | ")" | "<" | ">"
	       		 | "'" | '"' | "=" | "|" | "." | "," | ";" 
	       		 | "\" | "/" | ":" | "-" | "$" | "?" | "!" 
	       		 | "*" | "_" | "+" | "#" | "^" | "`" ;
	space = " " ;
	comma = "," ;
	tab = space, space, space, space ;
	newline = "\n" ;
	whitespace = space | tab | newline ;

	character = letter | number | symbol | whitespace ;
	text = {character} ;
	

	author = tab, "author:", space, text, newline ;
	collaborator = text | text, space, comma, space;
	collaborators = tab, "collaborators:", space, {collaborator}, newline ;
	date = tab, "date:", space, text, newline ;
	title = tab, "title:", space, text, newline ; 
	subtitle = tab, "subtitle:", space, text, newline ;

	school = tab, "school:", space, text, newline ;
	course = tab, "course:", space, text, newline ;
	due_date = tab, "due_date:", space, text, newline ;

	label = tab, tab, "label:", space, text, newline ;
	statement = tab, tab, "statement:", newline, tab, tab, tab, {character}, newline ;
	solution = tab, tab, "solution:", newline, tab, tab, tab, {character}, newline ;
	problem = tab, "problem:", newline, [label], statement, solution ;

	content = tab, tab, "content:", newline, tab, text, newline ;
	section = tab, "section:", newline, tab, title, content ;

	problem_set = "problem_set:", newline, author, [collaborators], [due_date], [title], [course], [school], {problem} ;

	memorandum = "memorandum:", newline, author, [collaborators], [date], title, [subtitle], {section} ;

	document = memorandum | problem_set ;
