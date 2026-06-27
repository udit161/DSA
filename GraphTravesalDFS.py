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

#DFS FUNCTION: 
                    
    def dfs(self, src):
        visited = [False] * self.size
        stack = []
        stack.append(src)
        visited[src] = True
        while(len(stack) != 0):
            u = stack.pop()
            print(u, end = " ")
            for v in range(self.size):
                if(self.mat[u][v] == 1 and visited[v] == False):
                    stack.append(v)
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