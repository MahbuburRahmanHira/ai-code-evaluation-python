import ast
import re
import cProfile
import timeit

# ----------------------------
# Step 4: Original logic
# ----------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    """Build linked list from Python list of integers."""
    dummy = ListNode(0)
    cur = dummy
    for x in arr or []:
        cur.next = ListNode(int(x))
        cur = cur.next
    return dummy.next

def add_two_numbers(l1, l2):
    """Add two numbers represented by linked lists in reverse order."""
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    a, b = l1, l2
    while a or b or carry:
        va = a.val if a else 0
        vb = b.val if b else 0
        total = va + vb + carry
        carry = total // 10
        cur.next = ListNode(total % 10)
        cur = cur.next
        if a: a = a.next
        if b: b = b.next
    return dummy.next

# ----------------------------
# Step 5: Solver wrapper with test cases
# ----------------------------
def solve():
    # Test cases: (lists representing numbers in reverse order)
    test_cases = [
        ([2,4,3], [5,6,4]),   # 342 + 465 = 807 => [7,0,8]
        ([0], [0]),           # 0 + 0 = 0 => [0]
        ([9,9,9,9], [1]),     # 9999 + 1 = 10000 => [0,0,0,0,1]
        ([1,8], [0]),         # 81 + 0 = 81 => [1,8]
    ]
    results = []
    for l1_list, l2_list in test_cases:
        l1 = build_list(l1_list)
        l2 = build_list(l2_list)
        res = add_two_numbers(l1, l2)
        out = []
        cur = res
        while cur:
            out.append(cur.val)
            cur = cur.next
        results.append(out)
    return results

# ----------------------------
# Profiling & Timing
# ----------------------------
if __name__ == "__main__":
    print("Profiling M2 Copilot solver...")
    def run_solver():
        solve()
    cProfile.runctx('run_solver()', globals(), locals())

    t = timeit.timeit(run_solver, number=10000)
    print(f"\nAverage execution time over 10000 runs: {t/10000:.8f} sec")

    # Output check
    outputs = solve()
    test_cases = [
        ([2,4,3], [5,6,4]),
        ([0], [0]),
        ([9,9,9,9], [1]),
        ([1,8], [0])
    ]
    for i, (l1, l2) in enumerate(test_cases):
        print(f"Input: {l1} + {l2} => Output: {outputs[i]}")
