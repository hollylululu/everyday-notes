#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from collections import deque

class BFSearcher:
    def __init__ (self):
        self.reached = list()
        self.queue = deque()

    def BFS (self, G, start):
        self.reached.append(start)
        self.queue.append(start)
        while not self.queue:
            v = self.queue.popleft()
            edges = G[v]
            for w in edges:
                if w not in self.reached:
                    self.reached.append(w)
                    self.queue.append(w)
        return self.reached

def main():
    import json
    import sys
    with open(sys.argv[1]) as f:
        data = json.load(f)
    searcher = BFSearcher()
    print searcher.BFS(data, 'start')

    
if __name__ == "__main__":
    main()

