Critique - Matt Cook


1) Do you think the language would benefit from having a less restrictive ordering with regard to header components like `date`, `due_date`, `collaborators`, `title, `subtitle`, etc.?

I honestly think it would, as you mentioned the ordering is a bit arbitrary. 
I'm not sure implementation-wise how much more difficult that would be, 
but at least computationally, despite being exponentially more complex,
I feel that there are few enough fields that it is unlikely to run into being a huge issue?
If it is actually the case that it would severely degrade performance, then possibly just make
sure that the error message for those cases will be informative enough to possibly even let you
know the correct order (like what it expects, and what it expects after that one too to give more information).


2) Do you find the language's [current installation and usage instructions](https://github.com/PaulDapolito/EasyTeX/blob/master/README.md) accessible and easily readable?

I personally think it is, and it looks simple enough for anyone who would need to start typesetting. I like the help
in telling how to get the dependencies, as that is something that would be important to someone that has never done
typesetting. 

I was able to follow the instructions and make the sample very easily! Also appreciate the notes to use sudo,
as that was the one "issue" I ran into (not really issue as I figured I would need it, but first ran without it
and it gave errors).

3) Do you think it is necessary to test EasyTeX's semantic functionality explicitly? As in, should I create automated tests that ensure that particular text input results in particular LaTeX output?

This sounds awfully tedious. I'm not sure if this would be necessary, as your overarching goal does not necessarily
have to be to emulate the typesetting of LaTeX, but essentially to have a typesetting tool that one can easily learn
to typeset their homework. As long as the typesetting looks good, it is perfectly fine (there are all sorts of LaTeX
templates anyways so I don't think a comparison would be too meaningful!). On that note, I would say it is worth also
user-testing on graders and professors to simply see what they think of the typesetting. Ask if there are aspects of the
tech memos and problem sets that they would like changed to look prettier or more natural.

4) What improvements would you make to EasyTeX's current design?

Honestly, I think it looks amazing right now, I am very impressed as to what you have as it is something I could really
see myself using if I end up writing more memorandums or problem sets (where we aren't given the template/problems like algs
or clinic). I would say the strict ordering thing is an important aspect to change, as I don't think LaTeX itself has such
strict ordering and just simply goes off of the tag? If not, that is probably still fine but I would just imagine myself
copy-pasting every time, which is not too big of a deal.

5) What improvements would you make to EasyTeX's current functional environment?

This would likely be entirely out of the scope of your project, but one of my favorite aspects to LaTeX's functional
environment is using Sublime Text to have syntax highlighting, as well as a way for pdf viewing immediately after compiling
within a sublime plugin/tool to show in Skim or SumatraPDF. It could be really cool to have a Sublime script to add EasyTeX as
a choosable language in Sublime for syntax highlighting, and the pdf part would be cool but maybe less important. Obviously, this is out of the scope
of what our projects should be, but just something to maybe keep in mind if you really want people to use it.