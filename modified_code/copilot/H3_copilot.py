import heapq
from itertools import count

# ----------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    """Build linked list from list of numbers."""
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

def merge_k_lists(node_lists):
    """Merge k sorted linked lists."""
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

# ----------------------------
def solve(lists_of_lists=None):
    """
    lists_of_lists: list of list of integers, e.g. [[1,4,5],[1,3,4],[2,6]]
    returns: merged sorted list as Python list
    """
    if lists_of_lists is None:
        return []

    node_lists = [build_list(lst) for lst in lists_of_lists]
    merged = merge_k_lists(node_lists)
    out = []
    cur = merged
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

# ----------------------------
# Ready-to-run wrapper with example input
# ----------------------------
def solve_wrapper():
    lists_of_lists = [[1,4,5],[1,3,4],[2,6]]
    return solve(lists_of_lists)

# ----------------------------
if __name__ == "__main__":
    print("H3 Copilot result:", solve_wrapper())  # Expected: [1,1,2,3,4,4,5,6]
