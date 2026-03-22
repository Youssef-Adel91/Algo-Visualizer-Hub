def tsp(N, s, distance, visited, cost):
    
    visited_key = tuple(visited)
    key = (s, visited_key)
    
    if key in cost:
        return cost[key]
    
    all_visited = True
    for i in range(len(N)):
        if visited[i] == 0:
            all_visited = False
            break
    
    if all_visited:
        return distance[s][0]
    
    # Recursive case
    min_cost = float('inf')
    
    for next_city in range(len(N)):
        if visited[next_city] == 0:
            visited[next_city] = 1
            
            total_cost = distance[s][next_city] + tsp(
                N, next_city, distance, visited, cost
            )
            
            if total_cost < min_cost:
                min_cost = total_cost
            
            visited[next_city] = 0  # backtrack
    
    cost[key] = min_cost
    return min_cost

# Main program
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

N = [0, 1, 2, 3]  # All cities
s = 0  # Starting city
visited = [0, 0, 0, 0]  # All unvisited initially
cost = {}  # Store computed costs

result = tsp(N, s, distance, visited, cost)
print(f"Minimum tour cost: {result}")