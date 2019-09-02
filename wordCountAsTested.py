#! /usr/bin/env python3

import sys
import os
import re
from collections import Counter #needed to count items in a list

#***To run this version of the program in the shell I had to use:
# exec(open(r"file path of wordCountAsTested.py").read())
# In my case: exec(open(r"C:\Users\alancew\Desktop\OS Project 1\wordCountAsTested.py").read()) ***

#open file by providing the path to the text file used (Lance Glaese assited me in this line of code as well as provided gerneral assistance in understanding python)
#reference: https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python
#note the file path needs to be changed in order to work properly
file = open(r"C:\Users\alancew\Desktop\OS Project 1\declaration.txt", "r", encoding="utf-8-sig")

#splits the string of the file by non-word characters that have one or more occurances into a list.
#reference used: https://www.w3schools.com/python/python_regex.asp
tokens = re.split('\W+', file.read().lower())
#sorts the list in alphabetical order.
tokenAlphabetized = sorted(tokens, key=str.lower)
#Counts each occurance of a string found in the list.
tokenCount = Counter(tokenAlphabetized)

# file path was hard coded in this version to test.
outputFile = open("outputFile.txt","w")
#iterate through the list displaying to the shell and saving to the output file.
for item in tokenCount.items():
    print("{} {}\n".format(*item)) #test line for terminal formated for as "{token} {number of token} \n".
    outputFile.write("{} {}\n".format(*item)) #same as previous line but writes to the file.
outputFile.close()

