#!/usr/bin/env python3

import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

class Graph:
    # A is the adjacency matrix, M the incidence matrix, M is optional
    def __init__(self, A, M = None):
        self.A = A
        self.M = M
        self.vertices = A.shape[0]

    # plot the graph
    def plot(self):
        adj = self.A
        coord = [[]]
        for i in range (0, adj.shape[0]):
            coord.append([random.random(), random.random()])
        p = Polygon(coord, facecolor = 'k')
        fig, ax = plt.subplots()
        ax.add_patch(p)
        ax.set_xlim([0,3])
        ax.set_ylim([0,3])
        plt.show()

    # tests if there are loops and returns their location in that case
    def ifLoop(self):
        adj = self.A
        test = False
        loopList = []
        for i in range (adj.shape[0]):
            for j in range (adj.shape[1]):
                if adj[i][j] != 0 and i == j:
                    test = True
                    loopList.append([i,1])
        if test == True:
            return test, loopList
        else:
            return test, 0

    # returns the number of vertices
    def vertices(self):
        return self.A.shape[0]

    # returns the number of edges
    def edges(self):
        adj = self.A
        edges = 0
        for i in range (adj.shape[0] // 2):
            for j in range (adj.shape[1]):
                edges += adj[i][j]
        return edges

    # tests if a graph contains double edges returns a boolean and the number of multiple edges of true
    def ifMultipleEdges(self):
        test = 0
        pos = []
        adj = self.A
        for vertex in adj:
            for i in range (len(vertex) // 2):
                if vertex[i] >= 2:
                    test += 1
                    pos.append([i + 1,vertex[i]])
        return test, pos

    # tests if the graph is connected i.e. if the graph is in one piece
    def ifConnected(self):
        adj = self.A
        for vertex in adj:
            if vertex.sum() == 0:
                return False
        return True

    # tests if the graph is Eulerian
    def ifEulerian(self):
        adj = self.A
        deg = 0
        k = 0
        for i in range (adj.shape[0]):
            for j in range (adj.shape[1]):
                deg += adj[i][j]
            if deg % 2 == 0:
                k += 1
        if k == adj.shape[0]:
            return True
        else:
            return False

    # tests if a simple graph is Hamiltonioan using Dirac's theorem
    def ifHamiltonian(self):
        adj = self.A
        k = 0
        if (self.ifLoop()[0] == False and self.ifMultipleEdges()[0] == False):
            for i in range (adj.shape[0] // 2):
                for j in range (i + 1, adj.shape[0]):
                    if (sum(adj[i]) + sum(adj[j]) >= adj.shape[0]):
                        k += 1
        if (k == (adj.shape[0] + 1)):
            return True
        else:
            return False

    # tests if the graph is a tree by checking that it is connected no cylces and has n-1 edges
    def ifTree(self):
        if (self.ifConnected() == True and self.edges() == self.vertices - 1):
            return True
        else:
            return False

if __name__ == "__main__":

    # graph definition with adjacency and incidence matrixes
    A = np.array([[0,1,0,1],[1,0,1,2],[0,1,0,1],[1,2,1,0]])
    A2 = np.array([[0,1,0,1],[1,0,1,1],[0,1,0,1],[1,1,1,0]])
    A3 = np.array([[0,1,0,1],[1,0,0,0],[0,1,0,1],[1,0,1,0]])
    B = np.array([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
    C = np.array([[1,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
    M = np.array([[1,0,0,1,0,0],[1,1,0,0,1,1],[0,1,1,0,0,0],[0,0,1,1,1,1]])

    graph1 = Graph(A)
#     graph1.plot()
    graph2 = Graph(A2)
    graph3 = Graph(A3)

    print(graph1.ifEulerian())
    print(graph1.edges())
    print(graph1.ifLoop())
    print(graph1.ifConnected())
    print(graph1.ifMultipleEdges())
    print("tree: ", graph1.ifTree())

    print(graph2.ifMultipleEdges())
    print(graph2.ifLoop())
    print(graph2.ifHamiltonian())
    print("tree: ", graph2.ifTree())

    print("tree: ", graph3.ifTree())
