import sys, ast, re
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def _parse_tree_list(s):
    s = s.strip()
    if not s:
        return []
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)):
            arr = list(v)
            res = []
            for x in arr:
                if x is None:
                    res.append(None)
                elif isinstance(x, str):
                    t = x.strip()
                    if t.lower() in ('null','none'):
                        res.append(None)
                    else:
                        try:
                            if '.' in t:
                                res.append(int(float(t)))
                            else:
                                res.append(int(t))
                        except Exception:
                            res.append(None)
                elif isinstance(x, (int, float)):
                    res.append(int(x))
                else:
                    res.append(None)
            return res
    except Exception:
        pass
    tokens = re.findall(r'null|None|-?\d+', s, flags=re.IGNORECASE)
    res = []
    for t in tokens:
        if t.lower() in ('null','none'):
            res.append(None)
        else:
            res.append(int(t))
    return res

def build_tree_from_list(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(int(x)) for x in arr]
    for i in range(len(nodes)):
        node = nodes[i]
        if node is not None:
            li = 2*i + 1
            ri = 2*i + 2
            if li < len(nodes):
                node.left = nodes[li]
            if ri < len(nodes):
                node.right = nodes[ri]
    return nodes[0]

def level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        n = len(q)
        level = []
        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

def solve():
    data = sys.stdin.read()
    if not data:
        print([]); return
    arr = _parse_tree_list(data)
    root = build_tree_from_list(arr)
    out = level_order(root)
    print(out)

if __name__ == "__main__":
    solve()