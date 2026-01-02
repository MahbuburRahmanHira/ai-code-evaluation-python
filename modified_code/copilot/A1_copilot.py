# ----------------------------
# Original Copilot logic preserved
# ----------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    parts = []
    def dfs(node):
        if node is None:
            parts.append('#')
            return
        parts.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ','.join(parts)

def deserialize(data):
    if not data:
        return None
    tokens = data.split(',')
    it = iter(tokens)
    def dfs():
        t = next(it)
        if t == '#':
            return None
        node = TreeNode(int(t))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()

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
