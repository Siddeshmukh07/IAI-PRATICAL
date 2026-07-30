from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['G', 'H'],
    'C': ['E', 'F'],
    'D': [],
    'G': ['I'],
    'H': [],
    'E': ['K'],
    'F': [],
    'I': [],
    'K': []
}

print("""
                S
              /   \\
             A     B
            / \\   / \\
           C   D G   H
          / \\    |
         E   F   I
        /
       K
""")

bfs(graph, 'S')