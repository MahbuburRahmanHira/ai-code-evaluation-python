import heapq
from typing import Dict, List, Tuple

# Type alias for the graph structure: 
# Adjacency list: node -> List[Tuple[neighbor, weight]]
Graph = Dict[int, List[Tuple[int, int]]]

def solve(graph: Graph, start: int) -> Dict[int, int]:
    """
    Implements Dijkstra's algorithm to find the shortest path from a starting 
    node to all other nodes in a weighted graph with non-negative edge weights.
    
    The graph is represented as an adjacency list: 
    {node: [(neighbor, weight), ...]}
    
    Returns a dictionary of {node: shortest_distance}.
    """
    
    # Check for empty graph
    if not graph:
        return {}
        
    # Check if the start node is in the graph
    if start not in graph:
        # If the start node is not a known node, return an empty set of distances 
        # or handle based on specific problem requirements.
        return {}
    
    # 1. Initialization
    
    # Dictionary to store the shortest distance found so far from 'start' to each node
    # Initialize all distances to infinity, except the start node which is 0.
    distances: Dict[int, int] = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority Queue (Min-Heap) stores tuples of (distance, node)
    # This allows efficient retrieval of the unvisited node with the smallest current distance.
    # Start with the source node.
    priority_queue: List[Tuple[int, int]] = [(0, start)]
    
    # 2. Main Loop
    while priority_queue:
        # Get the node with the smallest current distance (O(log V))
        current_distance, current_node = heapq.heappop(priority_queue)

        # Optimization (Lazy Deletion): If the distance extracted from the heap 
        # is greater than the recorded shortest distance, skip it. 
        # This occurs because we may have pushed a node multiple times with different distances.
        if current_distance > distances[current_node]:
            continue

        # 3. Explore Neighbors
        
        # Get the neighbors of the current node
        # Handle cases where a node exists in the distance dictionary but has no neighbors (empty list in graph)
        neighbors = graph.get(current_node, [])

        for neighbor, weight in neighbors:
            # Calculate the new distance to the neighbor through the current_node
            distance = current_distance + weight
            
            # Relaxation Step: If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                # Update the shortest distance
                distances[neighbor] = distance
                # Push the neighbor with the new shorter distance onto the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    # Remove nodes that were reachable but are not part of the input graph 
    # (if the problem context implies a fixed set of nodes).
    # Since we initialize based on `graph` keys, the output keys are all known nodes.
    
    # Filter out unreachable nodes (those still at infinity) for a cleaner result, 
    # although leaving them as float('inf') is also a valid representation.
    # For a typical answer, we will return the full dictionary with 'inf' for unreachable nodes.
    
    # Converting 'inf' back to a specific value or string is not required for a 
    # computational result, but if the problem expects all values to be int, 
    # we would need to adjust the infinity representation. 
    # We'll return the float('inf') for unreachable nodes.
    
    return distances

if __name__ == '__main__':
    # Test Case 1: Standard example graph
    graph_1 = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: []
    }
    start_1 = 0
    # Expected: {0: 0, 1: 3, 2: 1, 3: 4, 4: 7}
    print(f"Graph: {graph_1}, Start: {start_1}")
    print(f"Result: {solve(graph_1, start_1)}")

    # Test Case 2: Disconnected graph
    graph_2 = {
        1: [(2, 1)],
        2: [],
        3: [(4, 5)],
        4: []
    }
    start_2 = 1
    # Expected: {1: 0, 2: 1, 3: inf, 4: inf}
    print(f"Graph: {graph_2}, Start: {start_2}")
    print(f"Result: {solve(graph_2, start_2)}")
    
    # Test Case 3: Single node
    graph_3 = {5: []}
    start_3 = 5
    # Expected: {5: 0}
    print(f"Graph: {graph_3}, Start: {start_3}")
    print(f"Result: {solve(graph_3, start_3)}")