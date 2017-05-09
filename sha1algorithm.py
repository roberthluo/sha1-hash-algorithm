#!/usr/bin/env python



import io
import string
import struct
import ctypes

h0 = 0
h1 = 0
h2 = 0
h3 = 0
h4 = 0

_a = 0
_b = 0
_c = 0
_d = 0
_e = 0

def split(inputStr):
    #print "This is count"
    text_array = list(inputStr)
    for t in text_array:
        print t
    return text_array

def convert_to_ASCII(text_array):
    full_bin_str = ''

    #print "convert_to_ASCII"
    for t in text_array:
        #print long(ord(t))
        bin_val = bin(long(ord(t)))
        #print("bim", bin(long(ord(t))))
        bin_str = str(bin_val[2:])
        #print("bin str", bin_str)
        full_bin_str = full_bin_str+ bin_str
    #print full_bin_str

    #add '1' to the end
    full_bin_str = full_bin_str + '1'
    #print full_bin_str

    return full_bin_str

#part 6
#explaination: https://crypto.stackexchange.com/questions/41431/what-does-congruent-to-448-modulo-512-mean-for-padding-in-md5-hash-function?newreg=8172741ff41346fba02eabda35bbc27b
def append_zeros(full_bin_str):
        #Add zeros to end until length is congrunent to 448 mod 512
        orig_length = len(full_bin_str) - 1
        length = len(full_bin_str)
        while(length%512 != 0):
            length = len(full_bin_str)
            #print length
            full_bin_str = full_bin_str + '0'

        #print full_bin_str

        #append zeros
        orig_length_bin = bin(orig_length)
        orig_length_str = str(orig_length_bin[2:])
        #print ("orig_length_bin", orig_length, orig_length_str)

        #need to add 64 bits
        mess_padding = orig_length_str
        while(len(mess_padding) < 64):
            mess_padding = '0' + mess_padding
        #print ('length', len(mess_padding), mess_padding)

        total_message = full_bin_str + mess_padding
        #print total_message
        return total_message
        #Append original message length

#chunk message
#split each chunk to sixteen 32-bit words, return a list
def split_chunk(total_message, length = 32):
    #return (total_message[0+i:length+i] for i in range(0, len(total_message), length))
    chunk_array = []
    counter = 0
    temp_chunk = ''
    #print length
    for bits in total_message:
        temp_chunk = temp_chunk + bits
        if counter == length:
            counter = 0
            chunk_array.append(temp_chunk)
            temp_chunk = ''
        counter = counter+ 1

    #print chunk_array
    return chunk_array

def extend_to_eight_words(chunk_array):
    #starts off with 0, 2, 8, 13
    #hard coding to loop 16 times
    temp_chunk_array = chunk_array
    fourth = 13
    third = 8
    second = 2
    first = 0
    out = 17

    list_counter = range(80)
    for i in list_counter:
        list_counter[i] = False


    for i in range(79 - 16):
        #print 'value of i',i
        list_counter[fourth] = True
        list_counter[third] = True
        list_counter[second] = True
        list_counter[first] = True

        #print("index", fourth, third, second, first)
        fourth_word = int(temp_chunk_array[fourth])
        third_word = int(temp_chunk_array[third])
        second_word = int(temp_chunk_array[second])
        first_word = int(temp_chunk_array[first])
        #print "Words", fourth_word, third_word, second_word, first_word
        temp_word = fourth_word^third_word
        temp_word = temp_word^second_word
        temp_word = temp_word^first_word

        temp_chunk_array.append(temp_word)

        first = first + 1
        second = second + 1
        third = third + 1
        fourth = fourth + 1
        out = out + 1

        #print "Words len", len(temp_chunk_array)
        #while list_counter[first] :
        #    first = first + 1
        #while list_counter[second] or second == first:
        #    second = second + 1
        #while list_counter[third] or third == second or third == first:
        #    third = third + 1
        #while list_counter[fourth] or fourth == third or fourth == second or fourth == first:
        #    fourth = fourth + 1
        #while list_counter[out] or out == fourth or out == third or out == second or out == first:
        #    out = out + 1
    init_var_step_ten()

#Initialize some variables
def init_var():
    global h0
    global h1
    global h2
    global h3
    global h4

    h0 = 0b01100111010001010010001100000001
    h1 = 0b11101111110011011010101110001001
    h2 = 0b10011000101110101101110011111110
    h3 = 0b00010000001100100101010001110110
    h4 = 0b11000011110100101110000111110000

    #print "\n\n\n h0", h0
    #print "h1", h1
    #print "h2", h2
    #print "h3", h3
    #print "h4", h4

def init_var_step_ten():
    global _a
    global _b
    global _c
    global _d
    global _e
    #print "\n\n\n_b", h0
    _a = h0
    _b = h1
    _c = h2
    _d = h3
    _e = h4

def function_one():

    #prints in binary
    print "\n\n\n h4", h4
    print "\n\n\n _b", bin(_b)
    print "\n\n\n _c", bin(_c)
    out_one = _b & _c
    print "temp_step1", bin(out_one)

    out_two = (~_b) & _d
    print "temp_step", bin(out_two)
    _f = out_two | out_two

    print "_f",bin(_f)
    _k = 0b01011010100000100111100110011001

def function_two():
    print "\n\n\n _b", _b

    out_two = (_b ^ _c) ^ _d
    _k = 0b01101110110110011110101110100001

def function_three():
    print "\n\n\n _b", _b

    out_two = ((_b & _c) & (_b & _d)) | (C & D)

    _k = 0b10001111000110111011110011011100

def function_four():

    out_two = ((_b & _c) & (_b & _d)) | (C & D)

    _k = 0b11001010011000101100000111010110

def end_function():
    h0 = h0+_a;
    h1 = h1+_b;
    h2 = h2+_c;
    h3 = h3+_d;
    h4 = h4+_e;

    h0_hex = hex(h0)
    h1_hex = hex(h1)
    h2_hex = hex(h2)
    h3_hex = hex(h3)
    h4_hex = hex(h4)

    final_hash = h0_hex + h1_hex + h2_hex + h3_hex + h4_hex

class Sha1Hash(object):
    _message_byte_length = 0

    def __init__(self, message_byte_length):
        self._message_byte_length = message_byte_length

    def _left_rotate(n, b):
        #Left rotate a 32-bit integer n by b bits.
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
