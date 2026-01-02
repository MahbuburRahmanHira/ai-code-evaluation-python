import heapq
from typing import Dict, List, Tuple
import timeit
import cProfile

Graph = Dict[int, List[Tuple[int, int]]]

# ----------------------------
# Original Gemini logic preserved
# ----------------------------
def dijkstra_solver(graph: Graph, start: int) -> Dict[int, int]:
    if not graph or start not in graph:
        return {}
    distances: Dict[int, int] = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue: List[Tuple[int, int]] = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        neighbors = graph.get(current_node, [])
        for neighbor, weight in neighbors:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve():
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: []
    }
    start_node = 0
    return dijkstra_solver(graph, start_node)

if __name__ == '__main__':
    result = solve()
    print("A4_gemini result:", result)
