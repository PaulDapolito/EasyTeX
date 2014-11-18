#Critique on Design and Implementation- Mauricio Molina


###Language Design 
Overall feeling about the language design is that it is a fantastic start. I think it looks simple and is definitely hitting at the original goal you had of writing less code to do just as much work. I feel like anyone could look at any of your example EasyTex files as they are now and understand more or less what to expect the resulting file to look like. I also think it's great that you should be able to add more features and conversions from regular latex to EasyTex as you progress with your project. 


###Computational Model 
Overall great idea to simply compile EasyTex code down to latex code. The fact that a person could also be given latex code as well as PDF received using a latex compiler that does the work for you. My only question here is what you plan to give as output for features of latex that aren't currently available in EasyTex? How does the EasyTex compiler handle that? Are there simple error messages that you can give to let them know? Can a user simple use regular latex in EasyTex when there is no syntax in EasyTex to handle that situation? 


### Language Implementation
I think your error handling is really great and very helpful from what I've seen so far. The ability to give a small description of the error and the line number where the error occurs will be very helpful. 

I think creating a web based development environment for your language would be a
great idea, but I think it is fairly ambitious. However, based on where your language is at right now, I honestly think that you can do it, but the only down side is that I think an online development environment would be most useful and close to a final version the closer the actual DSL is to completion. You mentioned that there is a lot of latex stuff that hasn't been given an equivalent way to be written in EasyTex. Maybe try to spend more time finalizing the language until the end of this semester, then afterwards pick up the online development environment as a side project later. 


#Questions from Paul
### How might I go about creating tests for EasyTex semantics? 

It'd be really cool to have some of those struggling freshman to use EasyTex to do their assignment! Might be a bit of a commitment on their part. I think it'd be really interesting to see how EasyTex fares in a real world setting, and what isn't very intuitive to students. 


### What do you think about the samples that I have created so far? 

I think the samples are really really great. I would have loved to use EasyTex in the place of regular LaTex any day. My only question is if there is a strict enforcement of tabbing? If so, could that maybe have been an optional styling recommendation, but not required? Maybe having an end symbol for things that are nested in other elements? I can foresee this making for some frustrating errors for some users. 


### Any comments on initial syntax, layout, design? 

Honestly I think this is a really great project that you have a very good handle of. I really like that it's modular and can continue to be developed. I wouldn't be surprised if there was a legitimate community that would like to contribute to this DSL. 

