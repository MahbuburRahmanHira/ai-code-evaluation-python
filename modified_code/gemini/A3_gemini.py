from typing import List, Dict, Set, Optional
import timeit
import cProfile

# ----------------------------
# Original Gemini logic preserved
# ----------------------------
class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.word: Optional[str] = None 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

def word_search_solver(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0] or not words:
        return []

    ROWS, COLS = len(board), len(board[0])
    
    trie = Trie()
    for word in words:
        trie.insert(word)

    found_words: Set[str] = set()

    def dfs(r: int, c: int, node: TrieNode):
        char = board[r][c]
        if char not in node.children:
            return
        next_node = node.children[char]
        if next_node.word:
            found_words.add(next_node.word)
        board[r][c] = '#'
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                dfs(nr, nc, next_node)
        board[r][c] = char

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, trie.root)
    
    return list(found_words)

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
    words = ["oath","pea","eat","rain","hike","oak","tea"]
    return word_search_solver(board, words)

if __name__ == '__main__':
    result = solve()
    print("A3_gemini result:", result)
