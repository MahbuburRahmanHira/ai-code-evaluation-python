import heapq
from itertools import count

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr or []:
        cur.next = ListNode(int(x))
        cur = cur.next
    return dummy.next

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
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, next(counter), node.next))
    return dummy.next

# Wrapper
def solve_wrapper():
    lists_of_lists = [[1,4,5],[1,3,4],[2,6]]
    node_lists = [build_list(lst) for lst in lists_of_lists]
    merged = merge_k_lists(node_lists)
    out = []
    cur = merged
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

if __name__ == "__main__":
    print("H2 Copilot result:", solve_wrapper())  # Expected: [1,1,2,3,4,4,5,6]
