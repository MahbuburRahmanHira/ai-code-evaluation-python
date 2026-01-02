from typing import List, Dict, Set, Optional

# --- Trie Implementation ---

class TrieNode:
    """
    Node for the Trie structure.
    """
    def __init__(self):
        # A dictionary mapping character to child TrieNode
        self.children: Dict[str, 'TrieNode'] = {}
        # Stores the word if this node represents the end of a word
        self.word: Optional[str] = None 

class Trie:
    """
    Implementation of the Trie (Prefix Tree).
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word # Mark the end of the word

# --- Word Search Solver ---

def solve(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Finds words on the board using a combination of Trie and DFS.
    """
    if not board or not board[0] or not words:
        return []

    ROWS = len(board)
    COLS = len(board[0])
    
    # 1. Build the Trie
    trie = Trie()
    for word in words:
        trie.insert(word)

    # Use a set for O(1) word storage and duplicate avoidance
    found_words: Set[str] = set()

    def dfs(r: int, c: int, node: TrieNode):
        """
        Depth-First Search (DFS) for finding words on the board.
        r, c: current cell coordinates
        node: current TrieNode corresponding to the path from the start
        """
        char = board[r][c]
        
        # Check if the character leads to a valid path in the Trie
        if char not in node.children:
            return

        next_node = node.children[char]
        
        # If a word ends at this node, add it to the result set
        if next_node.word:
            found_words.add(next_node.word)
            # Optional optimization: to prevent re-finding the same word repeatedly 
            # while allowing the search to continue on the path (e.g., "cat" and "cater")
            # next_node.word = None 

        # Mark the current cell as visited by temporarily changing its value
        board[r][c] = '#'

        # Explore neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            # Check bounds and visited status (implicit: '#' is not in the Trie)
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                dfs(nr, nc, next_node)

        # Backtrack: Restore the cell's original character
        board[r][c] = char

    # 3. Start DFS from every cell on the board
    for r in range(ROWS):
        for c in range(COLS):
            # The DFS function handles the starting character check via 'trie.root'
            dfs(r, c, trie.root)
    
    return list(found_words)