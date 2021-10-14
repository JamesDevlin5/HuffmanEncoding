#!/usr/bin/env python3

from huffman import *


def test_basic():
    syms = "aaabbc"
    output = "0001010110"
    assert huffman_encode(syms) == output
