#!/usr/bin/env python3

from huffman import *


def test_basic():
    syms = "aaabbc"
    output = "0001010110"
    assert huffman_encode(syms) == output


def test_inverse_basic():
    syms = "aaabbc"
    output = "1110101001"
    assert huffman_encode(syms, inverse=True) == output
