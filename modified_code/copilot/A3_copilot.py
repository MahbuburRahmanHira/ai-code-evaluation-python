from typing import List, Dict

# ----------------------------
# Original Copilot logic preserved
# ----------------------------
class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.word: str = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

def word_search_solver(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0] or not words:
        return []

    trie = Trie()
    for w in words:
        if w:
            trie.insert(w)

    m, n = len(board), len(board[0])
    res = []

    def backtrack(i: int, j: int, parent: TrieNode):
        ch = board[i][j]
        node = parent.children.get(ch)
        if not node:
            return
        if node.word is not None:
            res.append(node.word)
            node.word = None

        board[i][j] = '#'
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                if board[ni][nj] in node.children:
                    backtrack(ni, nj, node)
        board[i][j] = ch

        if not node.children:
            parent.children.pop(ch, None)

    root = trie.root
    for i in range(m):
        for j in range(n):
            if board[i][j] in root.children:
                backtrack(i, j, root)

    return res

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve():
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words = ["oath","pea","eat","rain"]
    return word_search_solver(board, words)

if __name__ == "__main__":
    output = solve()
    print("A3_copilot result:", output)
