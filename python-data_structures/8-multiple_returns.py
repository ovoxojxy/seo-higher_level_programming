#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        length = len(sentence)
        first = None
    else:
        length = len(sentence)
        first = sentence[0]
    return length, first
