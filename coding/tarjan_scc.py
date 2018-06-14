#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division


class TarjanFinder:
    def __init__(self, data, start):
        self.low_link = dict()
        self.stack = list()
        self.index = dict()
        self.prev = dict()
        self.visited = dict()

        self.data = data
        self.start = start

        self.index[self.start] = 0
        self.counter = 0

    def tarjan(self):

        for v in self.data:
            if v not in self.prev:
                self.prev[v] = None
            if v not in self.index:
                self.index[v] = 0
            if v not in self.visited:
                self.visited[v] = 0

        for v in self.data:
            if not self.visited[v]:
                #print v
                self. tarjan_sub(v)

    def tarjan_sub(self, v):
        self.index[v] = self.counter
        self.low_link[v] = self.counter
        self.counter += 1
        #print self.counter
        self.stack.append(v)
        self.visited[v] = 1

        for u in self.data[v]:
            #print u + "~"
            if not self.visited[u]:
                self.tarjan_sub(u)
                self.low_link[v] = min(self.low_link[v], self.low_link[u])
            elif u in self.stack:
                self.low_link[v] = min(self.low_link[v], self.index[u])

        if self.low_link[v] == self.index[v]:
            while 1:
                node = self.stack.pop()
                print node
                if node == v:
                    print "------ End of an SCC ------"
                    break


def main():
    import json
    import sys
    with open(sys.argv[1]) as f:
        data = json.load(f)
    Tarjan = TarjanFinder(data, 'start')
    Tarjan.tarjan()


if __name__ == "__main__":
    main()

