import heapq

# ----------------------------
# Original ChatGPT logic preserved
# ----------------------------
def dijkstra(graph, start):
    if not graph or start not in graph:
        return {}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    start_node = 'A'
    return dijkstra(graph, start_node)

if __name__ == "__main__":
    result = solve()
    print("A4_chatgpt result:", result)
