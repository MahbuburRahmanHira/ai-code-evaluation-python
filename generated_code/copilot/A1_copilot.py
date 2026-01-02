class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve():
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
            try:
                t = next(it)
            except StopIteration:
                return None
            if t == '#':
                return None
            # try int then float then leave as string
            val = None
            try:
                val = int(t)
            except Exception:
                try:
                    fv = float(t)
                    val = int(fv) if fv.is_integer() else fv
                except Exception:
                    val = t
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

    return serialize, deserialize