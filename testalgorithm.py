#!/usr/bin/env python


import sha1algorithm




# Testing with Outputs

textArray = sha1algorithm.split("A Test")

full_bin_str = sha1algorithm.convert_to_ASCII(textArray)

total_message = sha1algorithm.append_zeros(full_bin_str)

chunked_message = sha1algorithm.split_chunk(total_message)

eight_words = sha1algorithm.extend_to_eight_words(chunked_message)
#print ('chunked_message', chunked_message)
