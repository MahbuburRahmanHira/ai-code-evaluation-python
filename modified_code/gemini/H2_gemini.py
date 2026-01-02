from typing import List, Optional
import heapq
import timeit
import cProfile

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Core solver (unchanged)"""
    min_heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(min_heap, (head.val, i, head))
    
    dummy_head = ListNode(0)
    current = dummy_head

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
    return dummy_head.next

# ----------------------------
# Helper functions (unchanged)
# ----------------------------
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

# ----------------------------
# Step 5: Wrapper for benchmarking
# ----------------------------
def solve_wrapper():
    test_case = [[1, 4, 5], [1, 3, 4], [2, 6]]
    node_lists = [list_to_linkedlist(lst) for lst in test_case]
    merged = solve(node_lists)  # core solver untouched
    return linkedlist_to_list(merged)

# ----------------------------
# Optional execution / profiling
# ----------------------------
if __name__ == "__main__":
    print("H2 Gemini result:", solve_wrapper())  # Expected: [1,1,2,3,4,4,5,6]

    def run_solver():
        solve_wrapper()

    print("Profiling H2 Gemini solver:")
    cProfile.runctx("run_solver()", globals(), locals())

    t = timeit.timeit(run_solver, number=1000)
    print(f"Average execution time over 1000 runs: {t/1000:.8f} sec")
