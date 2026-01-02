def solve(words=None):
    if not words:
        return []
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
