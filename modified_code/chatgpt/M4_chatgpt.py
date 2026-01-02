from collections import defaultdict

def group_anagrams(words):
    if not words: return []
    anagrams = defaultdict(list)
    for w in words:
        anagrams[''.join(sorted(w))].append(w)
    return list(anagrams.values())

def solve():
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    ]
    return [group_anagrams(words) for words in test_cases]
