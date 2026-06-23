class Graph:
    def __init__(self, vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size  = vertex

    def add_edge(self,src,dest):
        if( 0 <= src < self.size and 0<= dest < self.size):
            self.mat[src][dest] = 1
        else: 
            print("invalid edge")

    def print_graph(self):
        for i in self.mat:
            map(lambda x: print(x, end = " "), i)
            print()

    def print_adj(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.mat[i][j] == 1:
                    print(i, "->", j)

G = Graph(5)
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(0,3)
G.add_edge(0,4)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(3,4)
G.print_graph() 
G.print_adj()