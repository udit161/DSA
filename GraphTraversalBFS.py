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

#BFS FUNCTION: 

    def bfs(self, src):
        visited = [False] * self.size
        queue = []
        queue.append(src)
        visited[src] = True
        while(len(queue) != 0):
            u = queue.pop(0)
            print(u, end = " ")
            for v in range(self.size):
                if(self.mat[u][v] == 1 and visited[v] == False):
                    queue.append(v)
                    visited[v] = True
   


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print("DFS Traversal:")
g.dfs(2)