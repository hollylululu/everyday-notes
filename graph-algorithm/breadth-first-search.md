# Breadth-First Search

Breadth-first search is another commonly used graph search algorithm. It can be implemented by maintaining a queue.

## Pseudocode

```text
def BFS (graph, start):
    reached = {start}
    Q = queue data structure initially containing only the start vertex
    while Q not empty:
        v = Q.dequeue()
        for each edge v->w in graph:
            if w not in reached:
            add w to reached
            Q.enqueue(w)
    return reached
```



