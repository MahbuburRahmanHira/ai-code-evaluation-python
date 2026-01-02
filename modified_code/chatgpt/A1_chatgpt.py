# ----------------------------
# Original ChatGPT logic
# ----------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return ""
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    return ','.join(result)

def deserialize(data):
    if not data:
        return None
    from collections import deque
    nodes = data.split(',')
    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        if nodes[i] != "null":
            node.left = TreeNode(int(nodes[i]))
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] != "null":
            node.right = TreeNode(int(nodes[i]))
            queue.append(node.right)
        i += 1
    return root

# ----------------------------
# Unified solve wrapper for profiling
# ----------------------------
def solve():
    # Example input tree
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    s = serialize(root)
    new_root = deserialize(s)
    return new_root

if __name__ == "__main__":
    result = solve()
    print(serialize(result))
