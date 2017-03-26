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

class Sha1Hash(object):
    _message_byte_length = 0

    def __init__(self, message_byte_length):
        self._message_byte_length = message_byte_length

    def _left_rotate(n, b):
        #Left rotate a 32-bit integer n by b bits.
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
