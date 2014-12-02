# Critique for the week ending on November 30th

You did so much, I hope you still got to enjoy your Thanksgiving break!

## Response to Evaluation of work so far

Congrats on getting so much done. I'm glad the dictionary trick using 
`setResultsName` allowed you to create a more flexible ordering of header 
information, along with maintaining requirements for minimum information. The 
fact that you kept your implementation modular should really help if you want 
to work on allowing the user to be more picky about formatting, which you 
mention as a potential jumping-off point.

## Response to goals moving foward

I'm not quite sure what you mean by allowing the user to specify formatting 
and styling configurations. Do you mean to let users choose what package to 
use, because I don't see how your language can generalize the specific 
commands for each package into universal symbols. I'm afraid that this will go 
one of two ways: either it's too verbose and complex, and your easyTeX looses 
the simplicity it gained over traditional LaTeX, or it requires each user of a 
package to adapt the easyTeX interface to the specific package. If it's the 
first, I'm not sure that's worth it, unless you maintain a strict limit on the 
number of explicit controls. If it's the second, maybe you should focus on 
making it easy for people to adapt your language to these packages, rather 
than doing it yourself for a select few? I don't even know if that's possible, 
it's just a thought.

For the dependency and downloading problem, I feel the pain. I agree that the
time it takes to download and install LaTeX and all the other baggage that 
comes with is ridiculus. However, that aspect of the project is really not
DSL-related. It's important for the chance your language has of being useful
and used, but it's a design and packaging problem that doesn't really relate 
to what we've been doing in class. You've done so much already that this might
not be a problem, but it still feels like an odd focus for the end of the 
project. Besides, most people who would have use for your easyTeX might 
eventually want to learn LaTeX anyways, isn't that why you let them view and 
learn from the .tex source code? In this sense, downloading the full shabang 
is painful, but at least they'll have done it.

Your whitespace problem I think is a more appropriate place to focus your 
attention for the last leg of the project. It was a major factor of your 
initial design and seems to be a remaining weakness of your current design. It 
sounds like you've tried a lot of different ways to solve it, though, and have 
hit a wall. Could you make a sublime environment (syntax highlighting and 
suggested indentation included) to further encourage good indentation, or is 
that not quite what you're looking for? (Oh wait, you mention that as an 
option at the end of your evaluation, so you had thought of it - I second it, 
then, I think it might do much of what you're looking for.) It's not 
necessarilly a solution to the whitespace problem, but it would make the 
language more user friendly much faster than solving the indentation thing, 
which might then be reported a little bit. If you have an avenue to follow for 
the indentation though, I think that should maybe take priority. Would pyPEG 
have the functionality you need, or is that not an option that's really open 
at this point?

User testing is good, be nice to the frosh! 

The last main element you mention as a focus for the upcoming development is 
providing documentation/how-to information for newcomers to the language. This 
would be nice, a few paragraphs and a set of example documents should do the 
trick, and that wouldn't take too much time.

## Response to Notebook questions

**What things do you wish were different about the language's format and 
  specification?**

**Do you think it is of high priority to provide an environment for the 
  language?**

**How do you think I can make the installation/setup procedure easier for 
  EasyTeX users? What were your experiences like with the language's 
  installation/setup procedure?**
  
Currently, I'm having a slight problem. I have LaTeX on my machine, and 
python, and installed pip. However, it isn't recognizing pdflatex, which 
exists, so I'm confused. I noticed something minor while messing with this -
you should add a blank line at the end of `easytex.sh`, that shit 
doesn't pass linecheck! (I tried to `cat` it and it looked funny.) Minor 
problem, I can always open the generated TeX in the appropriate editor and 
generate the pdf from there, but that seems unecessarily confusing.

Your README instructions were helpful, thank you!

**What do you think of the language's error-handling and output? Did you find 
  it easy to identify and fix errors based on EasyTeX's output?**

**What do you think needs to be changed about the language, its runtime 
  process, or its installation/setup procedure?**

**What do you see as the most important aspect of the project in continuing 
  development?**


