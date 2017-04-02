#!/usr/bin/env python



import io
import string
import struct
import ctypes


def split(inputStr):
    print "This is count"
    text_array = list(inputStr)
    for t in text_array:
        print t
    return text_array

def convert_to_ASCII(text_array):
    bin_val = 0

    print "convert_to_ASCII"
    for t in text_array:
        print long(ord(t))
        print bin(long(ord(t)))
        bin_val += str(bin(int(ord(t))))
    print bin_val

class Sha1Hash(object):
    _message_byte_length = 0

    def __init__(self, message_byte_length):
        self._message_byte_length = message_byte_length

    def _left_rotate(n, b):
        #Left rotate a 32-bit integer n by b bits.
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
