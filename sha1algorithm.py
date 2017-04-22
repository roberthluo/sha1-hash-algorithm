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
#explaination: https://crypto.stackexchange.com/questions/41431/what-does-congruent-to-448-modulo-512-mean-for-padding-in-md5-hash-function?newreg=8172741ff41346fba02eabda35bbc27b
def append_zeros(full_bin_str):
        #Add zeros to end until length is congrunent to 448 mod 512
        orig_length = len(full_bin_str) - 1
        length = len(full_bin_str)
        while(length%512 != 0):
            length = len(full_bin_str)
            print length
            full_bin_str = full_bin_str + '0'

        print full_bin_str

        #append zeros
        orig_length_bin = bin(orig_length)
        orig_length_str = str(orig_length_bin[2:])
        print ("orig_length_bin", orig_length, orig_length_str)

        #need to add 64 bits
        mess_padding = orig_length_str
        while(len(mess_padding) < 64):
            mess_padding = '0' + mess_padding
        print ('length', len(mess_padding), mess_padding)

        total_message = full_bin_str + mess_padding
        print total_message
        #Append original message length

#chunk message


class Sha1Hash(object):
    _message_byte_length = 0

    def __init__(self, message_byte_length):
        self._message_byte_length = message_byte_length

    def _left_rotate(n, b):
        #Left rotate a 32-bit integer n by b bits.
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
