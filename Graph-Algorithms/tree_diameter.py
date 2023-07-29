from breadth_first_search import BFS

class vertex:
    def __init__(self,node_name:str, color:str, d:float, pi, neighbors:list):
        self.node_name = node_name
        self.color = color
        self.d = d
        self.pi =pi
        self.neighbors = neighbors

def tree_diameter(T:list):
    s = T[0]
    bfs_first = BFS(T, s.node_name)
    t, t_d = None, float("-inf")
    for vertex in bfs_first:
        if vertex.d > t_d:
            t_d = vertex.d
            t = vertex
    bfs_second = BFS(T, t.node_name)
    u, u_d = None, float("-inf")
    for vertex in bfs_second:
        if vertex.d > u_d:
            u_d = vertex.d
            u = vertex
    return u.d
