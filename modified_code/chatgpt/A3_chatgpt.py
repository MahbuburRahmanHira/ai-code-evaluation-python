# ----------------------------
# Original ChatGPT logic preserved
# ----------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

def find_words(board, words):
    if not board or not board[0] or not words:
        return []

    trie = Trie()
    for word in words:
        trie.insert(word)
    
    rows, cols = len(board), len(board[0])
    result = set()

    def dfs(r, c, node):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        char = board[r][c]
        if char not in node.children:
            return
        next_node = node.children[char]
        if next_node.word:
            result.add(next_node.word)
        board[r][c] = "#"
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(r + dr, c + dc, next_node)
        board[r][c] = char

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root)
    
    return list(result)

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve():
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    return find_words(board, words)

if __name__ == "__main__":
    result = solve()
    print("A3_chatgpt result:", result)
