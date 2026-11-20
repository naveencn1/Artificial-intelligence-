# CSA17 - Artificial Intelligence | Experiment 7 (Manual Ex. 1.7): Breadth First Search (BFS)
# Name            : V V Naveen Kumar
# Register Number : 192321018

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

def bfs(graph, start):
    visited = [start]
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nb in graph[node]:
            if nb not in visited:
                visited.append(nb)
                queue.append(nb)
    return order

print("BFS traversal from A:", bfs(graph, 'A'))


# ============================================================
# OUTPUT
# ============================================================
# BFS traversal from A: ['A', 'B', 'C', 'D', 'E', 'F']
