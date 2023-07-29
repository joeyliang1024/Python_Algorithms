# Breadth-first search (廣度優先搜尋)
class vertex:
    def __init__(self,node_name:str, color:str, d:float, pi, neighbors:list):
        self.node_name = node_name
        self.color = color
        self.d = d
        self.pi =pi
        self.neighbors = neighbors

def BFS(graph:list, start_vertex:str):
    # 初始化
    for vtx in graph:
        if vtx.node_name == start_vertex:
            vtx.color = "gray"
            vtx.d = 0
            vtx.pi = None
            queue = [vtx]
        else:
            vtx.color = "white"
            vtx.d = float("inf")
            vtx.pi = None

    result = []
    while len(queue) > 0:
        currentVertex = queue.pop(0)
        result.append(currentVertex)
        for neighbor in currentVertex.neighbors:
            for vtx in graph:
                if vtx.node_name == neighbor and vtx.color == "white":
                    vtx.color = "gray"
                    vtx.d = currentVertex.d + 1
                    vtx.pi = currentVertex
                    queue.append(vtx)
                    break
        currentVertex.color = "black"
    return result 
#Graph
graph = [
    vertex("A", "white", float("inf"), None, ["B", "D", "E"]),
    vertex("B", "white", float("inf"), None, ["A", "C"]),
    vertex("C", "white", float("inf"), None, ["B", "E"]),
    vertex("D", "white", float("inf"), None, ["A", "E"]),
    vertex("E", "white", float("inf"), None, ["A", "D", "F", "C"]),
    vertex("F", "white", float("inf"), None, ["E"])
]
result = BFS(graph,"A")
for r in result:
    print(r.node_name, end = " ")
print("")    
#['A', 'B', 'D', 'E', 'C', 'F']