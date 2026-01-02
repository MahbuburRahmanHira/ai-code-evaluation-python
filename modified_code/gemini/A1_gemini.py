from typing import Optional, List
from collections import deque

# ----------------------------
# Original Gemini logic preserved
# ----------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: Optional[TreeNode]) -> str:
    if not root:
        return ""
    queue = deque([root])
    result: List[str] = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("#")
    while result and result[-1] == "#":
        result.pop()
    return ",".join(result)

def deserialize(data: str) -> Optional[TreeNode]:
    if not data:
        return None
    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        parent = queue.popleft()
        if i < len(values) and values[i] != "#":
            parent.left = TreeNode(int(values[i]))
            queue.append(parent.left)
        i += 1
        if i < len(values) and values[i] != "#":
            parent.right = TreeNode(int(values[i]))
            queue.append(parent.right)
        i += 1
    return root

# ----------------------------
# Unified solve wrapper for profiling
# ----------------------------
def solve():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    s = serialize(root)
    new_root = deserialize(s)
    return new_root

if __name__ == "__main__":
    result = solve()
    print(serialize(result))
