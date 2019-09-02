Two versions of the wordCount program were uploaded. 
	-wordCount.py
	-wordCountAsTested.py
I was not able to run the 'python3 wordCount.py declaration.txt outputFile.txt' from the shell 
so I had to create another version of the program called wordCountAsTested.py to see if it ran.
In order to run the test the program I tested it by using the following command in the shell
and with a hard coded file path for the input text file in the code that would need to be changed
as well (this is noted in a comment in wordCountedAsTested.py):

exec(open(r"filepath").read())
Mine in specific was: exec(open(r"C:\Users\alancew\Desktop\OS Project 1\wordCountAsTested.py").read())

After execution I had the same results as the declarationKey.txt, except for one result at the
very beginning. It was reading any non-character symbol at the end of the file and counting
that as a result. This was discovered by creating a dummy file and testing with a sentence that
ends in a newline, period, and nothing. The only one not to display this bug was the one with
nothing at the end. I tested various different approaches using different patterns with
re.spilt(),re.findall(), and attempting to remove the result after tokenizing,
but was unsuccessful. If the neither of the above programs work I would be more than glad to
show a demonstration of my results.

-Alexander Wieczkowski
*(Lance Glaese assisted me in understanding how to run the python as well as general assistance
 in understanding python)*