from collections import deque
from typing import List, Set
import cProfile
import timeit

# ----------------------------
# Core solver (unchanged)
# ----------------------------
def solve(beginWord: str, endWord: str, wordList: List[str]) -> int:
    word_set: Set[str] = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])
    visited: Set[str] = {beginWord}

    while queue:
        current_word, steps = queue.popleft()
        if current_word == endWord:
            return steps

        for i in range(len(current_word)):
            original_char = current_word[i]
            for char_code in range(ord('a'), ord('z') + 1):
                next_char = chr(char_code)
                if next_char == original_char:
                    continue
                next_word = current_word[:i] + next_char + current_word[i+1:]
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))
    return 0

# ----------------------------
# Step 5 wrapper for profiling / testing
# ----------------------------
def solve_wrapper():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    return solve(beginWord, endWord, wordList)

# ----------------------------
# Optional execution / profiling
# ----------------------------
if __name__ == '__main__':
    print("H3 Gemini result:", solve_wrapper())  # Expected: 5

    def run_solver():
        solve_wrapper()

    print("Profiling H3 Gemini solver:")
    cProfile.runctx('run_solver()', globals(), locals())

    t = timeit.timeit(run_solver, number=1000)
    print(f"Average execution time over 1000 runs: {t/1000:.8f} sec")
