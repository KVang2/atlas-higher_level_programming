#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (None, len(sentence))
    first_char = sentence[0]
    return (first_char, len(sentence))
