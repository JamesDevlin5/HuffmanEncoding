#!/usr/bin/env python3
"""
Given a set of symbols and their weight, generates a prefix-free (binary) encoding tree with a minimum weight from the root.

> Example

the input string of symbols,

'aaabbc'

becomes the frequency table:

a | 3
b | 2
c | 1

which becomes the binary prefix tree:

a | 0
b | 10
c | 110

thus, the input string becomes the encoded binary sequence:

'0001010110'

"""

from collections import defaultdict


class FreqTable:
    """A container object measuring the number of occurrences of each symbol."""

    def __init__(self, syms):
        self._items = defaultdict(lambda: 0)
        for sym in syms:
            self._items[sym] += 1

    def items(self):
        """Gets a sorted generator of the input string of symbols."""
        return (
            k for k, _ in sorted(self._items.items(), key=lambda i: i[1], reverse=True)
        )


class Encoding:
    def __init__(self, table, prefix="1"):
        self._tbl = list(table.items())
        self._pref = prefix
        self._suff = "1" if prefix == "0" else "0"

    def _lookup(self, char):
        return self._tbl.index(char)

    def sym_to_str(self, sym):
        prefix_len = self._lookup(sym)
        return self._pref * prefix_len + self._suff


def huffman_encode(symbols, inverse=False):
    tbl = FreqTable(symbols)
    if inverse:
        pref = "0"
    else:
        pref = "1"

    encoding = Encoding(FreqTable(symbols), prefix=pref)
    result = ""
    for sym in symbols:
        result += encoding.sym_to_str(sym)
    return result
