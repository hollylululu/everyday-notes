# Graph Coloring

## Terminologies

* Clique: A subset of vertices that are all adjacent to each other. \(complete subgraph\)
* Chromatic number: the smallest number of colors needed to color a graph. Need to distinguish this term with coloring number. 
* Elimination ordering: Ordering of vertices so that earlier neighbors of every vertex form a clique. Not every graph has an elimination ordering. 
* Perfect elimination ordering: Ordering of the vertices of the graph such that, for each vertex v, v and the neighbors of v that occur after v in the order form a clique.
* Perfect graphs: Graphs whose chromatic number = max number of vertices in a clique, and it remains true if we delete any vertices. Perfect graphs have no odd holes, and no odd antiholes \(Hole in the complement graph\).
* Bipartite graph: a graph without odd-length cycle.

## Listing all maximal cliques - Bron-Kerbosch algorithm

First we distinguish between two concepts: 

* Maximum clique: a clique whose size is greater than or equal to the sizes of all cliques in a graph. Finding a maximum clique is an NP-Hard problem. 
* Maximal clique: a clique that you cannot add more vertices to. 

Therefore, a maximum clique is also a maximal clique by nature. However, not all maximal cliques are maximum. 

Bron-Kerbosch algorithm mis a recursive algorithm that outputs all maximal cliques in a graph. There are two variations of the algorithm - utilizing a pivot and visiting vertices by the degeneracy ordering. The algorithm maintains three sets of vertices:

1. R: clique that we build recursively in the algorithm. Starts with empty.
2. P: vertices that we might be able to add to R, but not yet in the clique. All vertices in P must be adjacent to all vertices in R.
3. X: vertices that we have already tried but can't add to R - otherwise would produce a clique we've already produced. We only keep vertices that are adjacent to all vertices in R.  

#### Basic form of BK algorithm

```text
def BK(R, P, X):
    //Base cases
    if P is empty and X is empty:
        output R
    return
    //main recursion
    //the for loop will be modified in the two variations of the algorithm
    for each v in P:
        BK(R Union {v}, P intersection N(v), X intersection N(v)):
            move v from P to X
```

Initially we start with BK\({}, all vertices, {}\)

#### First variation: with pivoting

```text

```

