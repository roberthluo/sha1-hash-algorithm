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
_f = 0
_k = 0

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

def extend_to_eighty_words(chunk_array):
    #starts off with 0, 2, 8, 13
    #hard coding to loop 16 times
    temp_chunk_array = []

    #loop through and make sure it is all binary type
    for item in chunk_array:
        temp_chunk_array.append(int(item, 2))


    print("temp chunk array", temp_chunk_array)
    fourth = 13
    third = 8
    second = 2
    first = 0
    out = 17

    list_counter = range(80)
    for i in list_counter:
        list_counter[i] = False

    print("temp chunk array", temp_chunk_array)

    for i in range(79 - 16):
        #print 'value of i',i
        list_counter[fourth] = True
        list_counter[third] = True
        list_counter[second] = True
        list_counter[first] = True

        print("type", type(temp_chunk_array[fourth]))
        #print("index", fourth, third, second, first)
        fourth_word = temp_chunk_array[fourth]
        third_word = temp_chunk_array[third]
        second_word = temp_chunk_array[second]
        first_word =temp_chunk_array[first]

        print "Words", fourth_word, third_word, second_word, first_word
        temp_word = fourth_word^third_word
        print "temp_word", temp_word
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

    #print("out", temp_chunk_array)

    init_var()
    init_var_step_ten()

    print 'extend to eight words', temp_chunk_array
    return temp_chunk_array

def main_loop(temp_chunk_array):
    print "main loop", temp_chunk_array


    for i in range(0, 79):
        if 0 <= i < 19:
            function_one()
            print "func one"
        if 20 <= i < 39:
            function_two()
        if 40 <= i < 59:
            function_three()
        if 60 <= i < 79:
            function_four()
        print "put together"
        put_together()

        end_function()

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
    global _f
    global _k
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
    return out_two

def function_two():
    print "\n\n\n _b", _b
    global _f
    global _k
    out_two = (_b ^ _c) ^ _d
    _f = out_two
    _k = 0b01101110110110011110101110100001
    return out_two

def function_three():
    print "\n\n\n _b", _b
    global _f
    global _k
    out_three = ((_b & _c) & (_b & _d)) | (_c & _d)
    _f = out_three
    _k = 0b10001111000110111011110011011100
    return out_three

def function_four():
    global _f
    global _k
    out_four = (_b ^ _c) ^ _d
    _f = out_four
    _k = 0b11001010011000101100000111010110
    return out_four

#right rotate
def ROR(x, n, bits = 32):
    mask = (2L**n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))

#left rotate
def ROL(x, n, bits=32):
    return ROR(x, bits - n, bits)

#step 11.2
def put_together():
    output = ROL(_a, 5, 64) + _f + _e + _k
    print bin(output)

    #check if output is longer than 32 bits
    #trucate the result
    #example : 100000100111110001101110010101010100 is more than 32 bits
    #output : 00100111110001101110010101010100
    # reassign values
    # E = D
    # D = c
    # C = 8 left Rotate 30
    # B = A
    # A = output
    print len(bin(output))

    if len(bin(output)) > 32:
        length = len(bin(output)) - 32


        global _e
        global _d
        global _c
        global _b
        global _a
        _e = _d
        _d = _c
        _c = ROL(_b, 30, 32)
        _b = _a
        _a = output


def end_function():

    global h0
    global h1
    global h2
    global h3
    global h4
    
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
    print "final_hash", final_hash

class Sha1Hash(object):
    _message_byte_length = 0

    def __init__(self, message_byte_length):
        self._message_byte_length = message_byte_length

    def _left_rotate(n, b):
        #Left rotate a 32-bit integer n by b bits.
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
