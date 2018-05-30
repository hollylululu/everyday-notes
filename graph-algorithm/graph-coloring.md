# Graph Coloring

## Terminologies

* Clique: A subset of vertices that are all adjacent to each other. \(complete subgraph\)
* Chromatic number: the smallest number of colors needed to color a graph.
* Elimination ordering: Ordering of vertices so that earlier neighbors of every vertex form a clique. Not every graph has an elimination ordering. 
* Perfect elimination ordering: Ordering of the vertices of the graph such that, for each vertex v, v and the neighbors of v that occur after v in the order form a clique.
* Perfect graphs: Graphs whose chromatic number = max number of vertices in a clique, and it remains true if we delete any vertices. Perfect graphs have no odd holes, and no odd antiholes \(Hole in the complement graph\).
* Bipartite graph: a graph without odd-length cycle.
* Chordal graph: A graph is perfect if and only if it has a perfect elimination ordering.

