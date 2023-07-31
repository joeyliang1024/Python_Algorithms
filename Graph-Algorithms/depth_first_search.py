# Breadth-first search (廣度優先搜尋)
class vertex:
    def __init__(self,node_name:str, color:str, d:float, pi, finish_time, neighbors:list):
        self.node_name = node_name
        self.color = color
        self.d = d
        self.pi =pi
        self.neighbors = neighbors
        self.f = finish_time

def DFS(graph:list):
    # 初始化
    for vtx in graph:
        vtx.color = "white"
        vtx.pi = None
    t = 0
    result = []
    for idx, vtx in enumerate(graph):
        if vtx.color == "white":
            DFS_visit(graph, graph[idx], t)
def DFS_visit(graph, u, t):
    t = t + 1
    u.d =t
    u.color = "gray"
    for neighbor in u.neighbors:
            for vtx in graph:
                 if vtx.node_name == neighbor and vtx.color == "white":
                      vtx.pi = u
                      DFS_visit(graph, vtx, t)
    u.color = "black"
    t = t + 1
    u.f = t
#Graph
graph = [
    vertex("A", "white", float("inf"), None, None, ["B", "D", "E"]),
    vertex("B", "white", float("inf"), None, None, ["A", "C"]),
    vertex("C", "white", float("inf"), None, None, ["B", "E"]),
    vertex("D", "white", float("inf"), None, None, ["A", "E"]),
    vertex("E", "white", float("inf"), None, None, ["A", "D", "F", "C"]),
    vertex("F", "white", float("inf"), None, None, ["E"])
]
DFS(graph)
for vtx in graph:
     print("u.d:{} u.f:{}".format(vtx.d, vtx.f))