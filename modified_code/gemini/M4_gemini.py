from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]):
    d = defaultdict(list)
    for s in strs:
        d["".join(sorted(s))].append(s)
    return list(d.values())

# --- Wrapper solve() for benchmark ---
def solve():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    return group_anagrams(strs)
