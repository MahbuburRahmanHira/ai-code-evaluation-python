import heapq
import math
from typing import Any, Dict, Iterable, List, Tuple

def _normalize_graph(graph) -> Dict[Any, List[Tuple[Any, float]]]:
    """
    Accepts common graph representations and returns adjacency dict:
    node -> list of (neighbor, weight)
    Supported input forms:
    - dict[node] = {neighbor: weight, ...}
    - dict[node] = [(neighbor, weight), ...]
    - dict[node] = list_of_neighbors (where neighbors are tuples)
    """
    adj = {}
    if graph is None:
        return adj
    if isinstance(graph, dict):
        for u, nbrs in graph.items():
            if nbrs is None:
                adj[u] = []
                continue
            # dict of neighbors
            if isinstance(nbrs, dict):
                adj[u] = []
                for v, w in nbrs.items():
                    try:
                        wv = float(w)
                    except Exception:
                        wv = float('inf')
                    adj[u].append((v, wv))
            else:
                # assume iterable of pairs
                adj[u] = []
                try:
                    for item in nbrs:
                        if item is None:
                            continue
                        if isinstance(item, tuple) or isinstance(item, list):
                            if len(item) >= 2:
                                v, w = item[0], item[1]
                                try:
                                    wv = float(w)
                                except Exception:
                                    wv = float('inf')
                                adj[u].append((v, wv))
                            else:
                                # single neighbor without weight -> treat as weight=1
                                v = item[0]
                                adj[u].append((v, 1.0))
                        else:
                            # neighbor is scalar -> assume weight 1
                            adj[u].append((item, 1.0))
                except TypeError:
                    # not iterable in expected way, skip
                    adj[u] = []
    else:
        # graph may be given as an edge list: iterable of (u, v, w)
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
                # ensure node presence for v
                adj.setdefault(v, [])
        except TypeError:
            # unknown format, return empty
            return {}
    # ensure every referenced node exists in adj
    nodes = set(adj.keys())
    for u, nbrs in list(adj.items()):
        for v, _ in nbrs:
            if v not in adj:
                adj.setdefault(v, [])
    return adj

def solve(graph, start):
    """
    graph: adjacency representation (see _normalize_graph)
    start: source node
    returns: dict mapping node -> shortest distance (float). Unreachable nodes will have math.inf.
    Raises ValueError if negative weights detected.
    """
    adj = _normalize_graph(graph)
    # include start even if not present
    adj.setdefault(start, [])
    # detect negative weights
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
        # stale entry
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