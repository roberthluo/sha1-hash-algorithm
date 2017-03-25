#!/usr/bin/env python



import io
import string


def split(inputStr):
    print "This is count"
    textArray = list(inputStr)
    for t in textArray:
        print t
    return textArray

def convertToASCII(textArray):
    for t in textArray:
        print ord(t)
