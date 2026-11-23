# CSA17 - Artificial Intelligence | Experiment 8 (Manual Ex. 1.8): Depth First Search (DFS)
# Name            : V V Naveen Kumar
# Register Number : 192321018

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for nb in graph[node]:
        if nb not in visited:
            dfs(graph, nb, visited)
    return visited

print("DFS traversal from A:", dfs(graph, 'A'))
