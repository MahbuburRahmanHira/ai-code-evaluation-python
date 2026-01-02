class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        current.next = ListNode(total_sum % 10)
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy_head.next

# --- Helpers ---
def list_to_linkedlist(arr):
    if not arr: return None
    head = ListNode(arr[0])
    cur = head
    for x in arr[1:]:
        cur.next = ListNode(x)
        cur = cur.next
    return head

def linkedlist_to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

# --- Wrapper solve() for benchmark ---
def solve():
    # default test case
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    return add_two_numbers(l1, l2)
