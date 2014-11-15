# November 11 Critique

To try to get my reaction to and understanding of your project, I will first go over my impressions od your work and project descriptions, and then I will reiterate things to more specifically respond to the questions you asked in your notebook.

## Impression on progress
I'm impressed at how quickly you've started diving into the implementation and difficulties of your project. I think you did well to start with error handling and tests, especially since you're approaching this with a bit of a "what's possible? what works?" approach. You are likely to find some semi-workable solutions, and your tests will help you identify their weaknesses. I do think you should be careful to treat this stage as a trial-and-error stage. By this I mean that you’ve jumped into trying to see what works, and it might be tempting to find a solution that solves one problem, and then move on. The danger there is to overlook more elegant solutions, and to get locked into a particular syntax that works for some things but makes others more complex. 

In your first comment in your description of the most pressing issues in your project, you refer to ‘the grammar at the top of the parser.py file’ but I don’t see an explicit comment of description of your grammar. Are you describing the list of terminals? I think a comment describing the overall structure would be nice, though I admit the code is pretty readable.

Concerning your error handling code, I agree that the current method is repetitive, but I don’t know enough about python errors to see how best to organize it differently. Is there a way to have broader classes of errors? You already organize them into categories in your directory structure. Could you have a single class for these and then have additions to the error message within each class, or is that simply not possible?




## Questions and Answers

I think your use of unit tests will prove very useful, and seems to be well adapted to your project. It will help you isolate problems at a lower level, but I think it might be more appropriate to focus your energy on creating test-documents. The line "author: Paul Dapolito IV **the Great**" should be parsed properly, and that's the use case for this section of your unit-tests, obviously, but I think a lot of the more difficult aspects of your project come from separating the document as a whole. Should something so small, without any document-content, even be accepted by your parser and then compiled? If so, do you know what the parsed tex and pdf output will look like?

The most difficult section will come from being able to tell where the name of the author ends and where the next section begins, that sort of thing. I think you should focus on the larger tests, such as the ones you describe in your Problem Set Tests, Memorandum Tests, Document Tests sections of your testing file. These aren’t unit-tests exactly, despite the name you give them, I think they are broader than that, but they do allow for testing a whole file, and how different sections combined.

In general, I think you should take a step back and consider your syntax and implementation as a whole, now that you have some experience with the tools and with the inevitable difficulties. This doesn’t have to take long, but it’s difficult to do because of the amount of work you’ve put in with the current syntax and resulting implementation in mind, so you have to separate yourself from that and be ok with having to write some things again if needed. You might find that a small change in your EasyTeX syntax will make it so much easier to implement all the features you want, without necessarily making it harder on the user’s end to write in your language. 



