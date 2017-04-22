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
    full_bin_str = ''

    print "convert_to_ASCII"
    for t in text_array:
        print long(ord(t))
        bin_val = bin(long(ord(t)))
        print("bim", bin(long(ord(t))))
        bin_str = str(bin_val[2:])
        print("bin str", bin_str)
        full_bin_str = full_bin_str+ bin_str
    print full_bin_str

    #add '1' to the end
    full_bin_str = full_bin_str + '1'
    print full_bin_str

    return full_bin_str

#part 6
def append_zeros(full_bin_str):
        #Add zeros to end until length is congrunent to 448 mod 512
        length = len(full_bin_str)
        while(length%512 != 0):
            length = len(full_bin_str)
            print length
            full_bin_str = full_bin_str + '0'

        print full_bin_str
        #append zeros

        #Append original message length

class Sha1Hash(object):
    _message_byte_length = 0

    def __init__(self, message_byte_length):
        self._message_byte_length = message_byte_length

    def _left_rotate(n, b):
        #Left rotate a 32-bit integer n by b bits.
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
