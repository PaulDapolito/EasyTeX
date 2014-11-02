# Project Plan

## Language evaluation

I envision EasyTeX as an end-to-end solution for typesetting technical work. This means that I want the DSL to encompass every step in the process from EasyTeX to LaTeX to PDF. 

The beginning of this pipeline is the design of EasyTeX's grammar and syntax. I want the syntax to be clean, whitespace delineated (rather than using brackets, semicolons, etc.), and most importantly, easy to use and understand. Then, I must create a tool which allows users to easily move from EasyTeX to PDF without ruling out the possibility that users might want access to the underlying LaTeX. 

I would like to assess EasyTeX's design along every step of this PDF creation process. I will do this mainly by soliciting feedback from my peers at Harvey Mudd College, all of whom have varying degrees of experiencing typesetting their work using LaTeX. While I have used LaTeX extensively, I will incorporate lots of feedback from my peers in order to reflect a wide range of opinions in designing EasyTeX to be user-friendly. More important than the opinions of experienced LaTeX users in assessing EasyTeX's design, however, will be feedback I receive from community members who have no experiencing typesetting their technical work. My entire goal in creating EasyTeX is to allow for the typesetting of problem sets and technical memorandums more easily and more efficiently. I want EasyTeX to remove the steep barrier to entry that currently exists for newcomers who wish to typeset their work. Thus, I will solicit feedback from many freshman at Harvey Mudd College, especially those who have never been able to or  have never attempted to typeset their work. This will allow me to make sure that my design for EasyTeX truly manifests the goals which I have for the DSL.

Another goal I have in mind for EasyTeX's design is to make sure the DSL is less clunky than LaTeX. I want EasyTeX documents to use less lines of code and allow users to create PDFs more quickly, so I will continually measure how EasyTeX performs against LaTeX along these metrics.  

In implementing EasyTeX, I will focus on testing at every step of the way. This will first require creating a parser for the language which outputs helpful errors messages and always instantiates a valid internal representation in Python. I will use Python's [pyparsing](http://pyparsing.wikispaces.com/) module to parse EasyTeX documents, and I will test my EasyTeX parser using Python's built-in unit testing framework ([unittest](https://docs.python.org/2/library/unittest.html)) to ensure that EasyTeX documents are parsed into valid internal representations. I insist on creating a parser which is robust in both its functionality and ability to help the user create valid EasyTeX documents, and this paradigm will be fueled by thorough unit testing. In order to ensure that I test every aspect of my parser, I also plan on measuring the code coverage of my testing using Python's [coverage](https://pypi.python.org/pypi/coverage) module.

From the internal representation yielded by the EasyTeX parser, EasyTeX will create a LaTeX document which will then be compiled into a PDF using pre-existing tools and methods. In order to ensure that EasyTeX's internal representation outputs syntactically valid LaTeX, I will implement thorough unit tests about the outputting process (EasyTeX's semantics). I envision EasyTeX's internal representation as a hierarchy of objects implemented in Python, and I will ensure that this representation outputs valid LaTeX by testing each Python class's outputting functionality individually. High quality implementation, in this case,  calls for the outputting of helpful error messages when some part of EasyTeX's internal representation encounters an issue, as well as the guarantee that a properly parsed internal representation yields valid LaTeX code. These error-checking measures, coupled by thorough unit testing and evaluations of code coverage, will yield an EasyTeX implementation which is of extremely high quality.

I will know EasyTeX has accomplished its goals when it is syntactically clean and extremely easy to use. My peers and other members of the Harvey Mudd College community will be quintessential in allowing me to evaluate EasyTeX's syntactic design and production pipeline. When I am satisfied with EasyTeX's design, I would like to create a web interface to allow users to enter EasyTeX and see a PDF generated in real-time, with syntactically incorrect lines highlighted (if applicable). I feel that the existence of such an interface alone would be a clear indication that I will have accomplished my goals for EasyTeX, as it would embody both of EasyTeX's convenience, practicality, and efficiency in an easily accessible medium.

## Implementation plan

I have already chosen a host language (Python) and target language (LaTeX) for my project, so my main focus on the project going forward is on particular implementation details. I will have to implement the internal representation, the parser, and the semantics (outputting functionality) of EasyTeX, as well as a thorough testing suite around the entire project and each individual component. In addition, I will have to provide an end-to-end way for users to create PDF documents from their EasyTeX files, and this will be provided via a web interface. I believe that the most difficult components of EasyTeX's implementation will be formulating a grammar for the language and implementing a robust parser. With these considerations in mind, I have contrived the following schedule for EasyTeX's development:

<table class="tg">
  <tr>
    <th class="tg-e3zv">Week Range</th>
    <th class="tg-e3zv">Action Items</th>
    <th class="tg-e3zv">Deliverables</th>
  </tr>
  <tr>
    <td class="tg-031e">10/26 - 11/1</td>
    <td class="tg-031e">1) complete project description<br>2) describe weekly plan<br>3) begin working on grammar<br>4) investigate unittest module</td>
    <td class="tg-031e">- Project plan<br>- Project description</td>
  </tr>
  <tr>
    <td class="tg-031e">11/2 - 11/8</td>
    <td class="tg-031e">1) complete grammar<br>2) implement internal representation<br>3) investigate pyparsing module<br>4) implement parser tests<br>5) begin implementing parser</td>
    <td class="tg-031e"><br>- Grammar<br>- Internal representation<br>- Parser tests<br></td>
  </tr>
  <tr>
    <td class="tg-031e">11/9 - 11/15</td>
    <td class="tg-031e">1) complete implementing parser<br>2) implement semantics tests<br>3) begin implementing outputting functionality (semantics)</td>
    <td class="tg-031e">- Parser<br>- Semantics tests</td>
  </tr>
  <tr>
    <td class="tg-031e">11/16 - 11/22</td>
    <td class="tg-031e">1) complete implementing outputting functionality<br>2) complete all testing<br>3) create prototype demonstration<br>4) begin implementing end-to-end PDF generation</td>
    <td class="tg-031e">- Outputting functionality<br>- EasyTeX prototype</td>
  </tr>
  <tr>
    <td class="tg-031e">11/23 - 11/29</td>
    <td class="tg-031e">1) implement end-to-end PDF generation<br>2) solicit peer feedback<br>3) implement design changes as per user feedback<br>4) begin working on preliminary evaluation</td>
    <td class="tg-031e"><br>- End-to-end PDF generation<br>- Changelog derived from feedback<br><br></td>
  </tr>
  <tr>
    <td class="tg-031e">11/30 - 12/6</td>
    <td class="tg-031e">1) complete preliminary evaluation<br>2) begin implementing web interface using Tornado</td>
    <td class="tg-031e">- preliminary evaluation</td>
  </tr>
  <tr>
    <td class="tg-031e">12/7 - 12/12</td>
    <td class="tg-031e">1) complete EasyTeX web interface<br>2) complete final write-up</td>
    <td class="tg-031e">- EasyTeX web interface<br>- final write-up</td>
  </tr>
</table>


## Teamwork plan 

I will be working alone, so this section of the document is not applicable.
