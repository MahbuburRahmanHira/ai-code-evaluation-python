from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res

# --- Helper ---
def create_tree(vals):
    if not vals: return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    root = nodes[0]
    i = 1
    for node in nodes:
        if node:
            if i < len(nodes): node.left = nodes[i]; i += 1
            if i < len(nodes): node.right = nodes[i]; i += 1
    return root

# --- Wrapper solve() for benchmark ---
def solve():
    root = create_tree([3, 9, 20, None, None, 15, 7])
    return level_order(root)
