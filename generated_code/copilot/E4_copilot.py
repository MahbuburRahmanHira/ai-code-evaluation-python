import sys, ast, re

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

def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    a, b = l1, l2
    while a and b:
        if a.val <= b.val:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next
        cur = cur.next
    cur.next = a or b
    return dummy.next

def _parse_list_literal(s):
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)):
            return list(v)
    except Exception:
        pass
    nums = re.findall(r'-?\d+', s)
    return [int(x) for x in nums] if nums else None

def _extract_two_lists(s):
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)) and len(v) == 2:
            a, b = v[0], v[1]
            if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                return list(a), list(b)
    except Exception:
        pass
    lists = re.findall(r'\[[^\]]*\]', s)
    if len(lists) >= 2:
        a = _parse_list_literal(lists[0])
        b = _parse_list_literal(lists[1])
        return a or [], b or []
    parts = [ln.strip() for ln in s.splitlines() if ln.strip()]
    if len(parts) >= 2:
        a = _parse_list_literal(parts[0]) or []
        b = _parse_list_literal(parts[1]) or []
        return a, b
    all_ints = re.findall(r'-?\d+', s)
    if len(all_ints) >= 2:
        mid = len(all_ints) // 2
        a = [int(x) for x in all_ints[:mid]]
        b = [int(x) for x in all_ints[mid:]]
        return a, b
    return [], []

def solve():
    data = sys.stdin.read()
    if not data:
        return
    a_list, b_list = _extract_two_lists(data)
    if a_list is None: a_list = []
    if b_list is None: b_list = []
    l1 = build_list(a_list)
    l2 = build_list(b_list)
    merged = merge_two_lists(l1, l2)
    out = []
    cur = merged
    while cur:
        out.append(cur.val)
        cur = cur.next
    print(out)

if __name__ == "__main__":
    solve()