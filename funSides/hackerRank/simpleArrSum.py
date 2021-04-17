#!/bin/python3

import os
import sys


#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #

    count = 0
    s = 0

    while count < ar_count and ar_count > 0:
        if 1000 > ar[count]:
            s += ar[count]
            count += 1
        else:
            count += 1
    return int(s)


# works only in hacker rank! change path to file!

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # this part opens the solution file basically, in a mode of write that enables one to edit the file first,
    # which passes it into stdin OS module in Python provides functions for interacting with the operating system.
    # OS comes under Python’s standard utility modules. This module provides a portable way of using operating system
    # dependent functionality.
    #
    # os.environ in Python is a mapping object that represents the user’s environment variables.
    # It returns a dictionary having user’s environmental variable as key and their values as value.
    #
    # os.environ behaves like a python dictionary, so all the common dictionary operations like get and set can be
    # performed. We can also modify os.environ but any changes will be effective only for the current process where
    # it was assigned and it will not change the value permanently.
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    # i understand the map function here: it basically creates an iterator like the for loop and runs the function
    # int(first argument) on each of the iterables given in the second argument as you would guess, rstrip removes
    # trailing whitespace of str input to avoid err split does a word separate taking two args : 1. The delimiter
    # with which to split <stoppage char;default is whitespace;and..it removes any empty str from result{removing
    # possibility of error}>, and the max number of splits to do, default being -1(which, when counted down,
    # never reaches zero), in the end spitting out a list thus the syntax for those two dots are: rstrip() → str
    # strip(del,max) → list and for the map… map(f(iter),iter) → object <iter>

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
