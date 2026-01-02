class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1: ListNode = None, l2: ListNode = None) -> ListNode:
    if l1 is None or l2 is None:
        l1_list, l2_list = [1,3,5], [2,4,6]
        l1 = ListNode(l1_list[0])
        current = l1
        for val in l1_list[1:]:
            current.next = ListNode(val)
            current = current.next
        l2 = ListNode(l2_list[0])
        current = l2
        for val in l2_list[1:]:
            current.next = ListNode(val)
            current = current.next

    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next

def listnode_to_list(head):
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items

if __name__ == '__main__':
    import timeit, cProfile

    test_cases = [([1,2,4],[1,3,4]), ([], [0]), ([], [])]

    def run_solver():
        for l1_list, l2_list in test_cases:
            l1 = ListNode(0) if not l1_list else ListNode(l1_list[0])
            cur = l1
            for val in l1_list[1:]:
                cur.next = ListNode(val)
                cur = cur.next
            l2 = ListNode(0) if not l2_list else ListNode(l2_list[0])
            cur = l2
            for val in l2_list[1:]:
                cur.next = ListNode(val)
                cur = cur.next
            solve(l1, l2)

    print("Profiling Merge Two Sorted Lists solver:")
    cProfile.runctx('run_solver()', globals(), locals())
    t = timeit.timeit(run_solver, number=10000)
    print(f"Average execution time: {t/10000:.8f} sec")

    for l1_list, l2_list in test_cases:
        l1 = ListNode(0) if not l1_list else ListNode(l1_list[0])
        cur = l1
        for val in l1_list[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        l2 = ListNode(0) if not l2_list else ListNode(l2_list[0])
        cur = l2
        for val in l2_list[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        merged = solve(l1, l2)
        print(f"Input: l1={l1_list}, l2={l2_list} -> Merged: {listnode_to_list(merged)}")
