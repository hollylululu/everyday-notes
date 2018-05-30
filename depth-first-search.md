# Depth-First Search

## Depth-First Search

Depth-First Search \(DFS\) is a commonly used graph search algorithm. It can be implemented recursively.

### Pseudocode:

```text
Initialize reached_set to {}
def visit (v):
    add v to reached_set
    for each edge v->w in G:
        if w not in reached_set:
            visit(w)
def DFS (G, start):
    reached_set = {}
    visit(start)
    return reached_set
```

Before we implement DFS in Python, let's see how graphs are represented in Python:

```text
{"start": ["a", "b", "c"], 
    "a": ["b", "d", "e"], 
    "b": ["c", "e", "f"], 
    "c": ["f"], 
    "d": ["e"], 
    "e": ["b"], 
    "f":["c"]}
```

The above dictionary shows a simple graph with 7 vertices and 13 edges.

### Python Implementation

```text
class DFSearcher: 
    def __init__ (self):
        self.reached_set = list()
    def DFS (self, G, start ):
        self.visit(start, G)
        return self.reached_set
    def visit (self, v, G):
        self.reached_set.append(v)
        edges = G[v]
        for w in edges:
            if w not in self.reached_set:
                self.visit(w, G)
```

We run the code on the above sample graph and get the following DFS ordering:

```text
['start', 'a', 'b', 'c', 'f', 'e', 'd']
```

### Runtime analysis

The above code uses a Python list to keep track of the resulting DFS order. We check if a vertex has been visited, if so, we do not visit it again. Therefore, each node will only be visited once. The runtime is thus O\(\|V\|\).

