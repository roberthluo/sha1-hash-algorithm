#!/usr/bin/env python


import sha1algorithm




# Testing with Outputs


textArray = sha1algorithm.split("A Test")

sha1algorithm.init_var()

full_bin_str = sha1algorithm.convert_to_ASCII(textArray)

total_message = sha1algorithm.append_zeros(full_bin_str)

chunked_message = sha1algorithm.split_chunk(total_message)

eighty_words = sha1algorithm.extend_to_eighty_words(chunked_message)

func_one = sha1algorithm.function_one()

func_two = sha1algorithm.function_two()

func_three = sha1algorithm.function_three()

func_four = sha1algorithm.function_four()

sha1algorithm.main_loop(eighty_words)

#print ('chunked_message', chunked_message)
