from collections import defaultdict

'''
Depth First Search uses STACK AND RECURSION
'''

def dfs(graph, start, visited, path):
    # Append the current node to the path list
    path.append(start)
    
    # Mark the current node as visited
    visited[start] = True
    
    # Iterate over the neighbors of the current node
    for neighbour in graph[start]:
        if not visited[neighbour]:
            # Recursively call dfs on the unvisited neighbor
            dfs(graph, neighbour, visited, path)
    
    return path

# Initialize an empty defaultdict to represent the graph
graph = defaultdict(list)

# Read the number of nodes (n) and edges (e) from input
n, e = map(int, input().split())

# Add each edge to the graph
for i in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  # Since the graph is undirected, add both directions

# Set the starting node
start = 'A'

# Create an empty defaultdict to keep track of visited nodes
visited = defaultdict(bool)

# Create an empty list to store the traversed path
path = []

# Call the dfs function with the starting node, visited nodes, and path
traversedpath = dfs(graph, start, visited, path)

# Print the traversed path
print(traversedpath)
