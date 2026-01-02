import sys, ast, re, heapq
from itertools import count

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr or []:
        try:
            cur.next = ListNode(int(x))
        except Exception:
            try:
                cur.next = ListNode(int(float(x)))
            except Exception:
                continue
        cur = cur.next
    return dummy.next

def parse_k_lists(s):
    s = s.strip()
    if not s:
        return []
    # try to parse as Python literal first
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)):
            # if it's a list of lists/tuples
            if all(isinstance(x, (list, tuple)) for x in v):
                return [[int(y) for y in x] for x in v]
            # if it's a flat list but contains nested lists as strings, fall through
    except Exception:
        pass
    # find all bracketed lists
    matches = re.findall(r'\[[^\]]*\]', s)
    if matches:
        res = []
        for m in matches:
            try:
                lst = ast.literal_eval(m)
                if isinstance(lst, (list, tuple)):
                    res.append([int(x) for x in lst])
            except Exception:
                nums = re.findall(r'-?\d+', m)
                if nums:
                    res.append([int(x) for x in nums])
        if res:
            return res
    # fallback: lines, each line is a list of ints
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    if len(lines) > 1:
        res = []
        for ln in lines:
            try:
                lst = ast.literal_eval(ln)
                if isinstance(lst, (list, tuple)):
                    res.append([int(x) for x in lst])
                    continue
            except Exception:
                pass
            nums = re.findall(r'-?\d+', ln)
            res.append([int(x) for x in nums])
        return res
    # last resort: try parse entire string as single list-of-lists string without proper separators
    return []

def merge_k_lists(node_lists):
    heap = []
    counter = count()
    for node in node_lists:
        if node:
            heapq.heappush(heap, (node.val, next(counter), node))
    dummy = ListNode(0)
    cur = dummy
    while heap:
        val, _, node = heapq.heappop(heap)
        cur.next = ListNode(val)
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, next(counter), node.next))
    return dummy.next

def solve():
    data = sys.stdin.read()
    lists = parse_k_lists(data)
    if not lists:
        print([]); return
    node_lists = [build_list(lst) for lst in lists]
    merged = merge_k_lists(node_lists)
    out = []
    cur = merged
    while cur:
        out.append(cur.val)
        cur = cur.next
    print(out)

if __name__ == "__main__":
    solve()