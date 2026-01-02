from typing import List, Dict

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.word: str = None  # store complete word at terminal node

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

def solve(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0] or not words:
        return []

    trie = Trie()
    for w in words:
        if w:  # skip empty words
            trie.insert(w)

    m, n = len(board), len(board[0])
    res = []

    def backtrack(i: int, j: int, parent: TrieNode):
        ch = board[i][j]
        node = parent.children.get(ch)
        if not node:
            return
        # check if we found a word
        if node.word is not None:
            res.append(node.word)
            # avoid duplicate finds
            node.word = None

        # mark visited
        board[i][j] = '#'
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                if board[ni][nj] in node.children:
                    backtrack(ni, nj, node)
        # restore
        board[i][j] = ch

        # pruning: if node has no children, remove it from parent
        if not node.children:
            parent.children.pop(ch, None)

    root = trie.root
    for i in range(m):
        for j in range(n):
            if board[i][j] in root.children:
                backtrack(i, j, root)

    return res