class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""
Graph using Adjacency list
"""
class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * vertices


    def add_edge(self,src, dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print(self):
        for i in range(self.v):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")



if __name__ =="__main__":
    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge()
