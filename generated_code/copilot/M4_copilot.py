import sys, ast, re
from collections import defaultdict

def _parse_words(s):
    s = s.strip()
    if not s:
        return []
    try:
        val = ast.literal_eval(s)
        if isinstance(val, str):
            return val.split()
        if isinstance(val, (list, tuple)):
            return [str(x) for x in val]
    except Exception:
        pass
    # find quoted words
    quoted = re.findall(r"'([^']*)'|\"([^\"]*)\"", s)
    if quoted:
        res = []
        for a,b in quoted:
            res.append(a if a != "" else b)
        if res:
            return res
    # fallback: split on common separators and whitespace
    parts = re.split(r'[\s,;\[\]\(\)]+', s)
    parts = [p for p in parts if p != ""]
    return parts

def group_anagrams(words):
    groups = {}
    for w in words:
        key = ''.join(sorted(w))
        if key in groups:
            groups[key].append(w)
        else:
            groups[key] = [w]
    return list(groups.values())

def solve():
    data = sys.stdin.read()
    words = _parse_words(data)
    out = group_anagrams(words)
    print(out)

if __name__ == "__main__":
    solve()