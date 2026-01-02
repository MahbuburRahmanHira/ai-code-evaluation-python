class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve_merge_lists(lists=None):
    if not lists:
        return None
    import heapq
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode(0)
    current = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

# Wrapper
def solve_wrapper():
    node1 = ListNode(1, ListNode(4, ListNode(5)))
    node2 = ListNode(1, ListNode(3, ListNode(4)))
    node3 = ListNode(2, ListNode(6))
    lists = [node1, node2, node3]

    new_head = solve_merge_lists(lists)
    result = []
    current = new_head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    print("H2 ChatGPT result:", solve_wrapper())  # Expected: [1,1,2,3,4,4,5,6]
