Author: Matt Cook

# Critique

# description.md

## Motivation

Overall, very well-written motivation! I find it especially useful to reference Jade and CoffeeScript as examples, as those do seem very similar. One concern I have is with " I feel that more students would typeset their work if the LaTeX learning curve wasn't so steep, and if the language was easier to access and create documents with. EasyTeX will try to remove this barrier of entry from typesetting technical work". It sounds like EasyTeX is mostly making the code prettier and easier to manage, not necessarily easier to learn. Along with that (and a concern I have with languages such as Jade or CoffeeScript), there is possibly the concern of lack of a "community", or help from others. With LaTeX, I really don't know anything about how to write in it, but for pretty much anything I can think of, I could Google it and find the appropriate syntax/package to use. This will not be the case with EasyTeX (that is, of course, unless it catches on!) and so it would seem the learning curve can still be difficult unless there is good and easy to use documentation, or a very intuitive mapping from LaTeX to EasyTeX.

## Language Domain

I personally agree this is both a sufficiently narrow, but useful domain that you have specified! I do think this will involve a fair bit a research to really determine what type of things in LaTeX as well as its packages people use for technical documents. Could you give examples of DSLs that are in existence fro creating technical LaTeX documents? It would be good to address why those were not successful.

## Language Design

Do you have an idea for what interface will be used to transcompile to LaTeX (command line, GUI, etc.)? LaTeX is nice because of the different ways to do this (e.g. personally, I love using Sublime Text and Skim/SumatraPDF to compile and view PDF files. Would it be possible to use existing LaTeX tools?). 

Is there a particular reason for the use of Python (not commenting on whether it is a good or bad choice, but just wondering whether you have looked into the easiest language to do this type of transcompiling)? I do notice now that you actually mentioned that you have investigated pretty deeply into Python, but basically I just wondering whether there were other, "inferior" (for this domain) choices that you were deciding between. By "output well-formatted LaTeX code", do you mean human-readable, or simply that it is then compilable to a PDF (from the example computations it looks like the former)? I do like that the errors messages sound like they could possibly be more useful than LaTeX's currently are, which is definitely a plus!

## Example Computations 

The first example of EasyTeX looks good! One thing I am wondering is with two lines for "section:" and then "title:". It seems like those could possible be merged into one where you just name the section? Same goes for the second one with "problem" and "label". 

# plan.md

## Language evaluation

One feature that could be interesting that could maybe help address my earlier issue of having no community is to also allow a reverse pipeline of LaTeX to EasyTex. Say you have a template you already want to use, but not sure how to use it in EasyTeX (or too lazy to translate it all), so you might just want to go in reverse. This would make it easier for some more experienced people of LaTeX to understand how to use EasyTeX. Not sure how easy this would actually be to do, but maybe something to keep in mind as you design/implement the language!

## Implementation Plan

Overall, your implementation plan looks good! It looks sufficiently ambitious, and only concern might be whether you should implement web interface at all versus possibly the need for encompassing more language features (as it seems like it could be difficult to initially encompass everything in LaTeX for technical documents). Also, I would possibly solicit peer feedback earlier to see what people think of the language? Otherwise, it will simply be our group guiding how you should design EasyTeX, which is not quite what you are looking for (or at least not your primary target audience).


# grammar.md

Overall, this looks great and is awesome that you have this already. I know it isn't necessarily complete yet, but make sure  that your EBNF is strict about your whitespace, which seemed to be one of the main points of EasyTeX. It seems important to outline how the whitespace delineation will work (can it be with both tabs and whitespaces? can you have multiple new lines between each?, etc.). 

# Notebook

Unforunately, I am unfamiliar with any of the Python testing frameworks, so I could not confidently tell you what I would think is best. Looking briefly at each of the ones you mentioned, they seem to all sufficient for your needs. Main thing I might look for is how much help you can find online for each (how big of a community each has).

I think this is a very cool project! As noted before, I am a little concerned with the practicality of such a language in terms of tradeoffs between learning curve and usefulness of the language. With your current example computations, it seems like the learning curve would be fine, but I suppose I am a bit worried that it could get more complicated in terms of the formatting of a tech memo or problem set (i.e. adding pictures, trees, tables, etc.).

The project plan overall looks good, but as I mentioned before main thing I would suggest is to have more peer feedback from your target audience of people that write technical documents but unfamiliar with LaTeX.









