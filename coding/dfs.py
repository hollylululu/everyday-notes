#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import collections
from collections import defaultdict
import timeit
import string
import argparse

class DFSearcher:
    def __init__ (self):
        self.reached_set = list()

    def DFS (self, G, start):
        self.visit(start, G)
        return self.reached_set


    def visit (self, v, G):
        self.reached_set.append(v)
        edges = G[v]
        for w in edges:
            if w not in self.reached_set:
                self.visit(w, G)

def main():
    import json
    import sys
    with open(sys.argv[1]) as f:
        data = json.load(f)
    searcher = DFSearcher()
    print searcher.DFS(data, 'start')

    

if __name__ == "__main__":
    main()

