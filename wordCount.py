#! /usr/bin/env python3

import sys
import os
import re
from collections import Counter #needed to count items in a list

#Lance Glaese assited me in gerneral assistance in understanding python

inputFileName = sys.args[1] # text file to be read from is the 1st argument
outputFileName = sys.args[2] # text file to be saved to is the 2nd argument

#opens designated file to write to
with open(inputFileName, 'r') as textfile:
    #splits the string of the file by non-word characters that have one or more occurances into a list.
    #reference used: https://www.w3schools.com/python/python_regex.asp
    tokens = re.split('\W+', textFile.read().lower())

    #sorts the list in alphabetical order.
    tokenAlphabetized = sorted(tokens, key=str.lower)
    
    #Counts each occurance of a string found in the list
    tokenCount = Counter(tokenAlphabetized)
    
#opens designated file to write to
with open(outputFileName, 'w') as outputFile:
    for item in tokenCount.items():
        print("{} {}\n".format(*item)) #test line for terminal
        outputFile.write("{} {}\n".format(*item)) #same as previous line but write to the file
