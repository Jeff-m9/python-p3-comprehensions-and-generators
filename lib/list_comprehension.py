#!/usr/bin/env python3

def return_evens(num_list):
    final_list = [n for n in num_list if n % 2 == 0]
    return final_list

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]