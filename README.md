# A Graph class that checks some properties

## Definitions

### • Simple graph
A simple graph $G$ consists of a non-empty finite set $V(G)$ of elements called vertices (or nodes), and a finite set $E(G)$ of distinct unordered pairs of distinct elements of $V(G)$ called edges. We call $V(G)$ the vertex set and $E(G)$ the edge set of $G$.

### • Graph
A general graph or just graph is a simple graph that can contain a loop if it has edges that are joins to themselves.

### • How do we represent graphs ?
To represent graphs, we will use matrix representations:
- If $G$ is a graph with vertices labelled $\\{1,2,...,n\\}$, its adjacency matrix $A$ is the $n \times n$ matrix whose $ij$-th entry is the number of edges joining vertex $i$ and vertex $j$.
- If the edges are labelled $\\{1,2,...,m\\}$, its incidence matrix $M$ is the $n \times m$ matrix whose $ij$-th entry is $1$ if vertex $i$ is incident to edge $j$, and $0$ otherwise. That matrix is optionnal.

<img width="677" alt="Capture d’écran 2023-02-28 à 13 53 46" src="https://user-images.githubusercontent.com/126407732/221862222-1a7d1216-7685-4966-91c9-4c65b2036e8d.png">

## Properties

### • Connectedness

A graph is connected if it cannot be expressed as the union of two graphs, and disconnected otherwise.

<img width="574" alt="Capture d’écran 2023-02-28 à 13 50 11" src="https://user-images.githubusercontent.com/126407732/221858836-0c375d58-e4ba-4b73-9f7f-f9d967b8eca3.png">

For example the $G_1 \cup G_2$ graph above is a disconnected graph since it's the union of $G_1$ and $G_2$ that are two connected graphs.
