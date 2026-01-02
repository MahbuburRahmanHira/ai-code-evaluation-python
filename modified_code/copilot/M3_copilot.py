import ast
import re
from collections import deque
import cProfile
import timeit

# ----------------------------
# Step 4: Original logic
# ----------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def _parse_tree_list(s):
    """Parse a string into a list suitable for tree building, handling None/null."""
    s = s.strip()
    if not s:
        return []
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)):
            res = []
            for x in v:
                if x is None:
                    res.append(None)
                elif isinstance(x, str):
                    t = x.strip()
                    if t.lower() in ('null', 'none'):
                        res.append(None)
                    else:
                        try:
                            res.append(int(float(t)) if '.' in t else int(t))
                        except Exception:
                            res.append(None)
                elif isinstance(x, (int, float)):
                    res.append(int(x))
                else:
                    res.append(None)
            return res
    except Exception:
        pass
    # fallback regex parsing
    tokens = re.findall(r'null|None|-?\d+', s, flags=re.IGNORECASE)
    res = [None if t.lower() in ('null', 'none') else int(t) for t in tokens]
    return res

def build_tree_from_list(arr):
    """Build binary tree from level-order list with None for missing nodes."""
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    for i, node in enumerate(nodes):
        if node is not None:
            li, ri = 2*i + 1, 2*i + 2
            if li < len(nodes):
                node.left = nodes[li]
            if ri < len(nodes):
                node.right = nodes[ri]
    return nodes[0]

def level_order(root):
    """Return level-order traversal of a binary tree as list of lists."""
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

# ----------------------------
# Step 5: Solver wrapper
# ----------------------------
def solve():
    # Multiple test cases: strings representing trees
    test_cases = [
        "[1,2,3,null,4]",
        "[3,9,20,null,null,15,7]",
        "[]",
        "[1]"
    ]
    results = []
    for s in test_cases:
        arr = _parse_tree_list(s)
        root = build_tree_from_list(arr)
        results.append(level_order(root))
    return results

# ----------------------------
# Profiling & Timing
# ----------------------------
if __name__ == "__main__":
    print("Profiling M3 Copilot solver...")
    def run_solver():
        solve()
    cProfile.runctx('run_solver()', globals(), locals())

    t = timeit.timeit(run_solver, number=10000)
    print(f"\nAverage execution time over 10000 runs: {t/10000:.8f} sec")

    # Output check
    outputs = solve()
    test_cases = [
        "[1,2,3,null,4]",
        "[3,9,20,null,null,15,7]",
        "[]",
        "[1]"
    ]
    for i, s in enumerate(test_cases):
        print(f"Input: {s} => Output: {outputs[i]}")
