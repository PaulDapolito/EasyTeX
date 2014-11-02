# Project plan

## Language evaluation

I envision EasyTeX as an end-to-end solution for typesetting technical work. This means that I want the DSL to encompass every step in the process from EasyTeX to LaTeX to PDF. 

The beginning of this pipeline is the design of EasyTeX itself. I want the syntax to be clean, whitespace delineated (rather than using brackets, semicolons, etc.), and most importantly, easy to use. Then, I must create a tool which allows users to easily move from EasyTeX to PDF without ruling out the possibility that users might want access to the underlying LaTeX. 

I would like to assess EasyTeX's design at every step of this PDF creation process. I will do this mainly by soliciting feedback from my peers at Harvey Mudd College, all of whom have varying degrees of experiencing typesetting their work using LaTeX. While I have used LaTeX extensively, I will incorporate lots of feedback from my peers in order to reflect a wide range of opinions in designing EasyTeX to be user-friendly. 

More important than the opinions of experienced LaTeX users in assessing EasyTeX's design will be feedback I receive from community members who have no experiencing typesetting their technical work. My entire goal in creating EasyTeX is to allow for the typesetting of problem sets and technical memorandums more easily and more efficiently. I want EasyTeX to remove the steep barrier to entry that currently exists for newcomers who wish to typeset their work. Thus, I will solicit feedback from many freshman at Harvey Mudd College, especially those who have never been able to or who have never attempted to typeset their work. This will allow me to make sure that my design for EasyTeX truly manifests the goals which I have for the DSL.

Another goal I have in mind for EasyTeX's design is to make sure the DSL is less clunky than LaTeX. I want EasyTeX documents to use less lines of code and allow users to create PDFs more quickly, so I will continually measure how EasyTeX performs against LaTeX along these metrics.  

In implementing EasyTeX, I will focus on testing at every step of the way. This will first require creating a parser for the language which outputs helpful errors messages and instantiates a valid internal representation in Python. I will use Python's [pyparsing](http://pyparsing.wikispaces.com/) module to parse EasyTeX documents, and I will test my EasyTeX parser using Python's built-in unit testing framework ([unittest](https://docs.python.org/2/library/unittest.html)) to ensure that EasyTeX documents are parsed into valid internal representations. I insist on creating a parser which is robust in both its functionality and ability to help the user create valid EasyTeX documents, and this paradigm will be fueled by thorough unit testing. In order to ensure that I test every aspect of my parser, I also plan on measuring the code coverage of my testing using Python's [coverage](https://pypi.python.org/pypi/coverage) module.

From the internal representation yielded by the EasyTeX parser, EasyTeX will create a LaTeX document which will then be compiled into a PDF using pre-existing tools and methods. In order to ensure that EasyTeX's internal representation outputs syntactically valid LaTeX, I will implement thorough unit tests about the outputting process. I envision EasyTeX's internal representation as a hierarchy of objects implemented in Python, and I will ensure that this representation outputs valid LaTeX by testing each Python class's outputting functionality. High quality implementation, in this case,  calls for the outputting of helpful error messages when some part of EasyTeX's internal representation encounters an issue. I plan on performing thorough tests on the instantiation of any part of EasyTeX's internal representation with the intention of being able to efficiently direct the user to problematic input. I feel that these error-checking measures, coupled by thorough unit testing and evaluations of code coverage, will yield an EasyTeX implementation which is of extremely high quality.


I will know EasyTeX has accomplished its goals when it is syntactically clean and extremely easy-to-use. My peers and other members of the Harvey Mudd College community will be quintessential in allowing me to evaluate EasyTeX's syntactic design. When I am satisfied with EasyTeX's design, I would like to create a web interface to allow users to enter EasyTeX and see the generated PDF in real-time. This interface would highlight which lines are syntactically incorrect, if applicable, to allow the user to easily fix their input. I feel that such an interface would be a clear indication that I will have accomplished my goals for EasyTeX, as it would embody both of EasyTeX's convenience and practicality in an easily accessible medium.

## Implementation plan



## Teamwork plan 

I will be working alone, so this section of the document is not applicable.