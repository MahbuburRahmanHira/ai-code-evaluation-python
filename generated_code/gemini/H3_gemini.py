from collections import deque
from typing import List, Set

def solve(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Finds the length of the shortest transformation sequence from beginWord to endWord 
    using Breadth-First Search (BFS).
    """
    # 1. Edge Case: If endWord is not in the wordList, no transformation is possible.
    word_set: Set[str] = set(wordList)
    if endWord not in word_set:
        return 0

    # 2. Initialization for BFS
    # Queue for BFS, storing tuples of (word, steps)
    queue = deque([(beginWord, 1)])
    
    # Set to keep track of visited words to prevent cycles and redundant work
    # Start by marking beginWord as visited.
    visited: Set[str] = {beginWord}
    
    # 3. BFS Loop
    while queue:
        current_word, steps = queue.popleft()

        # Check for the end condition
        if current_word == endWord:
            return steps

        # Generate all possible next words by changing one character
        for i in range(len(current_word)):
            original_char = current_word[i]
            
            # Try changing the character at position i to every letter from 'a' to 'z'
            for char_code in range(ord('a'), ord('z') + 1):
                next_char = chr(char_code)
                
                # Only proceed if the character is actually changed
                if next_char == original_char:
                    continue
                    
                # Create the potential next word
                next_word_list = list(current_word)
                next_word_list[i] = next_char
                next_word = "".join(next_word_list)

                # Check if the next_word is a valid, unvisited word from the dictionary
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))
                    
    # 4. If the queue becomes empty and endWord was not reached
    return 0

if __name__ == '__main__':
    # Test Case 1
    beginWord_1 = "hit"
    endWord_1 = "cog"
    wordList_1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    # Expected: 5 (hit -> hot -> dot -> dog -> cog OR hit -> hot -> lot -> log -> cog)
    print(f"Input: {beginWord_1}, {endWord_1}, {wordList_1}, Output: {solve(beginWord_1, endWord_1, wordList_1)}")

    # Test Case 2
    beginWord_2 = "hit"
    endWord_2 = "cog"
    wordList_2 = ["hot", "dot", "dog", "lot", "log"] # cog is missing
    # Expected: 0
    print(f"Input: {beginWord_2}, {endWord_2}, {wordList_2}, Output: {solve(beginWord_2, endWord_2, wordList_2)}")

    # Test Case 3
    beginWord_3 = "a"
    endWord_3 = "c"
    wordList_3 = ["a", "b", "c"]
    # Expected: 2 (a -> c) or (a -> b -> c), but the smallest is (a -> c)
    print(f"Input: {beginWord_3}, {endWord_3}, {wordList_3}, Output: {solve(beginWord_3, endWord_3, wordList_3)}")