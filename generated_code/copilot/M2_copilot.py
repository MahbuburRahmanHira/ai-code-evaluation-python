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

def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    a, b = l1, l2
    while a or b or carry:
        va = a.val if a else 0
        vb = b.val if b else 0
        s = va + vb + carry
        carry = s // 10
        cur.next = ListNode(s % 10)
        cur = cur.next
        if a: a = a.next
        if b: b = b.next
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
    s = s.strip()
    try:
        v = ast.literal_eval(s)
        if isinstance(v, (list, tuple)) and len(v) == 2:
            a, b = v[0], v[1]
            if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                return [int(x) for x in a], [int(x) for x in b]
    except Exception:
        pass
    lists = re.findall(r'\[[^\]]*\]', s)
    if len(lists) >= 2:
        a = _parse_list_literal(lists[0]) or []
        b = _parse_list_literal(lists[1]) or []
        return a, b
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    if len(lines) >= 2:
        a = _parse_list_literal(lines[0]) or []
        b = _parse_list_literal(lines[1]) or []
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
    res = add_two_numbers(l1, l2)
    out = []
    cur = res
    while cur:
        out.append(cur.val)
        cur = cur.next
    print(out)

if __name__ == "__main__":
    solve()