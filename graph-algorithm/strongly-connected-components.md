# Strongly Connected Components

## Definition

* Strongly connected components: Vertex u and v are strongly connected to each other, if there exists a path u-&gt;v and v-&gt;u.
* Strong connectivity relation is reflexive, symmetric and transitive.

## Tarjan's SCC algorithm

Tarjan's SCC algorithm takes linear time and uses one pass of a DFS. It adds two additional pieces of information to the original DFS: DFS numbering \(preorder\) and lowlink numbers. It uses a stack to keep track of the DFS visiting. 

