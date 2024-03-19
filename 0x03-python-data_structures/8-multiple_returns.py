#!/usr/bin/python3

def multiple_returns(sentence):
    s_len = len(sentence)
    first_char = "None" if s_len == 0 else sentence[0]

    return (s_len, first_char)
