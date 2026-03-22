"""
Floyd-Warshall Algorithm - Student Implementation Template
Complete the TODO sections to implement the algorithm
"""

def floyd_warshall(graph, vertices):
    
    infinity = 999999
    
   # Step 1: Initialize distance matrix with infinity
    distance = [[infinity] * vertices for _ in range(vertices)]
    
    # Step 2: Diagonal is 0
    for i in range(vertices):
        distance[i][i] = 0
    
    # Step 3: Fill direct edges
    for src in graph:
        for weight, dest in graph[src]:
            distance[src-1][dest-1] = weight
    
    # Step 4: Floyd-Warshall core
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance


def print_matrix(matrix, size):
    """
    Print matrix in a nice format - DO NOT MODIFY
    """
    print("     ", end="")
    for j in range(size):
        print("V" + str(j+1) + "   ", end="")
    print()
    
    for i in range(size):
        print("V" + str(i+1) + " ", end="")
        for j in range(size):
            if matrix[i][j] == 999999:
                print("  ∞  ", end="")
            else:
                print(str(matrix[i][j]).rjust(4) + " ", end="")
        print()


def print_shortest_paths(matrix, size):
    """
    Print all shortest paths - DO NOT MODIFY
    """
    print()
    print("=" * 60)
    print("SHORTEST PATHS BETWEEN ALL PAIRS")
    print("=" * 60)
    print()
    
    for i in range(size):
        for j in range(size):
            if i != j:
                if matrix[i][j] == 999999:
                    print("V" + str(i+1) + " -> V" + str(j+1) + 
                          ": No path exists")
                else:
                    print("V" + str(i+1) + " -> V" + str(j+1) + 
                          ": " + str(matrix[i][j]))


# TEST CASE 1
print("TEST CASE 1: Simple graph with 4 vertices")
print("=" * 60)
print()

graph1 = {
    1: [(-2, 3)],
    2: [(4, 1), (3, 3)],
    3: [(2, 4)],
    4: [(-1, 2)]
}

vertices1 = 4
result1 = floyd_warshall(graph1, vertices1)

print("Final distance matrix:")
print_matrix(result1, vertices1)
print_shortest_paths(result1, vertices1)


print()
print()
print("TEST CASE 2: Another graph")
print("=" * 60)
print()

graph2 = {
    1: [(5, 2), (2, 3)],
    2: [(1, 4)],
    3: [(3, 4)],
    4: []
}

vertices2 = 4
result2 = floyd_warshall(graph2, vertices2)

print("Final distance matrix:")
print_matrix(result2, vertices2)
print_shortest_paths(result2, vertices2)