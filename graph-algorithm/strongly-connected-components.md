# Strongly Connected Components

## Definition

* Strongly connected components: Vertex u and v are strongly connected to each other, if there exists a path u-&gt;v and v-&gt;u.
* Strong connectivity relation is reflexive, symmetric and transitive.

## Tarjan's SCC algorithm

Tarjan's SCC algorithm takes linear time and uses one pass of a DFS. It adds two additional pieces of information to the original DFS: DFS numbering \(preorder\) and lowlink numbers. It uses a stack to keep track of the DFS visiting.

### Pseudocode

```text
def tarjan_main (G, s):
\\initializations
    stack = empty
    counter = 0
    for all v in G:
        index[v] = 0
        visited[v] = false
    index[s] = 0

\\iterations
    for all v in G:
        if not visited[v]:
            tarjan_sub(v)

def tarjan_sub(v):
\\update the status of the currently visited vertex
    index[v] = counter
    low[v] = counter
    counter ++
    stack.push(v)
    visited[v] = true
    for all v->u in G.edges:
        if not visited[u]:
            tarjan_sub(u)
            low[v] = min(low[v], low[u])
        elif u in stack:
            low[v] = min(low[v], index[u])

\\finish iterating all neighbors
    if low[v] == index[v]:
        pop vertices off stack until vertex == v
```

### Python Implementation

I am only showing the main recursion function here, since the initialization part is rather trivial.

```python
def tarjan_sub(self, v):
    self.index[v] = self.counter
    self.low[v] = self.counter
    counter += 1
    self.stack.append(v)
    self.visited[v] = 1

    for u in self.date[v]:
        if not self.visited[u]:
            tarjan_sub(u)
            self.low[v] = min(self.low[v], self.low[u])
        elif u in self.stack:
            self.low[v] = min(self.low[v], self.index[u])
    if self.low[v] == self.index[v]:
        while 1:
            node = self.stack.pop()
            print node
            if node == v:
                print "------ End of an SCC ---------"
                break
```

### Example

For the following input graph:

```text
{"start": ["a", "b", "c"],     "a": ["b", "d", "e"],     "b": ["c", "e", "f"],     "c": ["f"],     "d": ["e"],     "e": ["b"],     "f":["c"]}
```

The graph looks like:

![Sample input graph](../.gitbook/assets/example%20%281%29.jpg)

The output of the program will be:

```text
f c 
------ End of an SCC ------ 
e b 
------ End of an SCC ------ 
d 
------ End of an SCC ------ 
a 
------ End of an SCC ------ 
start 
------ End of an SCC ------
```

### Runtime Analysis

Each vertex and edge will be visited once and only once. Thus, it is easy to see that the runtime for the algorithm is O\(E+V\).

