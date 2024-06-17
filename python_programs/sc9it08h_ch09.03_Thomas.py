def floyd_warshall(graph):
    # Number of vertices in the graph
    n = len(graph)
    
    # Applying Floyd Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

# Function to print the graph
def print_graph(graph):
    for row in graph:
        print(" ".join(f"{val:5}" if val != 500 else "  inf" for val in row))

# Function to read graph from user input
def read_graph():
    n = int(input("Enter the number of nodes: "))
    graph = []
    print("Enter the adjacency matrix row by row (use 500 for infinity):")
    for i in range(n):
        row = list(map(int, input(f"Row {i}: ").strip().split()))
        graph.append(row)
    return graph

# Read the graph from user input
graph = read_graph()

print("\nOriginal graph:")
print_graph(graph)

# Run Floyd-Warshall algorithm
floyd_warshall(graph)

print("\nGraph after running Floyd-Warshall algorithm:")
print_graph(graph)

# Get the start and end nodes from the user
start_node = int(input("Enter the start node: "))
end_node = int(input("Enter the end node: "))

# Output the length of the shortest path from start_node to end_node
print(f"\nThe length of the shortest path from node {start_node} to node {end_node} is: {graph[start_node][end_node]}")