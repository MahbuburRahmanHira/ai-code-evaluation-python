# ----------------------------
# Original ChatGPT logic
# ----------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1, l2):
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

# ----------------------------
# Step 5 wrapper
# ----------------------------
def solve_wrapper():
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    l2 = ListNode(2, ListNode(4, ListNode(6)))
    merged_head = solve(l1, l2)
    result = []
    current = merged_head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    result = solve_wrapper()
    print("Merged list (ChatGPT):", result)  # Expected: [1,2,3,4,5,6]
