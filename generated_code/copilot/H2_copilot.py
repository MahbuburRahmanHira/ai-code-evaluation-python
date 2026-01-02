import sys, ast, re
import heapq
from itertools import count

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    if not arr:
        return None
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(int(x))
        cur = cur.next
    return dummy.next

def _parse_list_literal(s):
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)):
            res = []
            for x in v:
                if x is None:
                    res.append(None)
                elif isinstance(x, (int, float)):
                    res.append(int(x))
                elif isinstance(x, str) and re.fullmatch(r'-?\d+', x.strip()):
                    res.append(int(x.strip()))
                else:
                    res.append(None)
            return res
    except Exception:
        pass
    nums = re.findall(r'-?\d+', s)
    return [int(x) for x in nums] if nums else None

def _extract_k_lists(s):
    s = s.strip()
    if not s:
        return []
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)):
            # If it's a list of lists like [[1,2],[3,4],[]]
            if all(isinstance(x, (list, tuple)) for x in v):
                return [[int(y) for y in list(x)] for x in v]
            # If it's a tuple/list of two where each is list, handle
            if len(v) > 0 and all(isinstance(x, (int, float)) for x in v):
                return [list(v)]
    except Exception:
        pass
    # find all bracketed lists
    lists = re.findall(r'\[[^\]]*\]', s)
    if lists:
        res = []
        for L in lists:
            parsed = _parse_list_literal(L)
            res.append(parsed if parsed is not None else [])
        return res
    # fallback: split lines, each line a list or numbers
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    if lines and len(lines) > 1:
        res = []
        for ln in lines:
            parsed = _parse_list_literal(ln)
            res.append(parsed if parsed is not None else [])
        return res
    # last resort: try to parse as single list
    single = _parse_list_literal(s)
    if single is not None:
        # if single contains nested lists as string, attempt to split by delimers
        if any(isinstance(x, (list, tuple)) for x in single):
            return [list(x) for x in single if isinstance(x, (list, tuple))]
        return [single]
    return []

def merge_k_lists(lists_of_nodes):
    heap = []
    counter = count()
    for node in lists_of_nodes:
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
    if not data:
        print([]); return
    lists = _extract_k_lists(data)
    if lists is None:
        lists = []
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