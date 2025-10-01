
# Input nodes
n = int(input("Enter number of nodes: "))
nodes = []
for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    nodes.append(node)

# Input edges
edges = []
e = int(input("Enter number of edges: "))
for i in range(e):
    u = input("Enter first node of edge: ")
    v = input("Enter second node of edge: ")
    edges.append((u, v))

# Create adjacency matrix
matrix = [[0] * n for _ in range(n)]
for u, v in edges:
    if u in nodes and v in nodes:
        i, j = nodes.index(u), nodes.index(v)
        matrix[i][j] = 1
        matrix[j][i] = 1
    else:
        print(f"Invalid edge ({u}, {v}) skipped.")

# Create adjacency list
adj_list = {node: [] for node in nodes}
for u, v in edges:
    if u in adj_list and v in adj_list:
        adj_list[u].append(v)
        adj_list[v].append(u)

# Show adjacency matrix
print("\nAdjacency Matrix:")
print("  " + "  ".join(nodes))
for i in range(n):
    print(nodes[i], matrix[i])

# Show adjacency list
print("\nAdjacency List:")
for node in nodes:
    print(f"{node}: {adj_list[node]}")

# DFS using adjacency matrix
def dfs(start):
    visited = []
    stack = [nodes.index(start)]

    while stack:
        current = stack.pop()
        if nodes[current] not in visited:
            visited.append(nodes[current])
            for neighbor in range(n - 1, -1, -1):
                if matrix[current][neighbor] == 1 and nodes[neighbor] not in visited:
                    stack.append(neighbor)
    return visited

# BFS using adjacency list
def bfs(start):
    visited = []
    queue = [start]

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            for neighbor in adj_list[current]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

# Traversals
start_node = input("\nEnter starting node: ")
if start_node not in nodes:
    print("Invalid start node.")
else:
    print("\nDFS (Adjacency Matrix):")
    print(" -> ".join(dfs(start_node)))

    print("\nBFS (Adjacency List):")
    print(" -> ".join(bfs(start_node)))

