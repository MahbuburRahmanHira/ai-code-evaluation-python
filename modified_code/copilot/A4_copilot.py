import heapq
import math
from typing import Any, Dict, List, Tuple

# ----------------------------
# Original Copilot logic preserved
# ----------------------------
def _normalize_graph(graph) -> Dict[Any, List[Tuple[Any, float]]]:
    adj = {}
    if graph is None:
        return adj
    if isinstance(graph, dict):
        for u, nbrs in graph.items():
            if nbrs is None:
                adj[u] = []
                continue
            if isinstance(nbrs, dict):
                adj[u] = []
                for v, w in nbrs.items():
                    try:
                        wv = float(w)
                    except Exception:
                        wv = float('inf')
                    adj[u].append((v, wv))
            else:
                adj[u] = []
                try:
                    for item in nbrs:
                        if item is None:
                            continue
                        if isinstance(item, (tuple, list)) and len(item) >= 2:
                            v, w = item[0], item[1]
                            try:
                                wv = float(w)
                            except Exception:
                                wv = float('inf')
                            adj[u].append((v, wv))
                        elif isinstance(item, (tuple, list)) and len(item) == 1:
                            v = item[0]
                            adj[u].append((v, 1.0))
                        else:
                            adj[u].append((item, 1.0))
                except TypeError:
                    adj[u] = []
    else:
        try:
            for edge in graph:
                if not edge:
                    continue
                if len(edge) >= 3:
                    u, v, w = edge[0], edge[1], edge[2]
                elif len(edge) == 2:
                    u, v = edge[0], edge[1]
                    w = 1.0
                else:
                    continue
                try:
                    wv = float(w)
                except Exception:
                    wv = float('inf')
                adj.setdefault(u, []).append((v, wv))
                adj.setdefault(v, [])
        except TypeError:
            return {}
    for u, nbrs in list(adj.items()):
        for v, _ in nbrs:
            if v not in adj:
                adj.setdefault(v, [])
    return adj

def dijkstra_solver(graph, start):
    adj = _normalize_graph(graph)
    adj.setdefault(start, [])
    for u, nbrs in adj.items():
        for _, w in nbrs:
            if w < 0:
                raise ValueError("Graph contains negative weight; Dijkstra not applicable.")
    dist = {node: math.inf for node in adj}
    dist[start] = 0.0
    visited = set()
    heap = [(0.0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if d > dist.get(u, math.inf):
            continue
        for v, w in adj.get(u, []):
            if v in visited:
                continue
            nd = d + w
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

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
    return dijkstra_solver(graph, start_node)

if __name__ == "__main__":
    result = solve()
    print("A4_copilot result:", result)
