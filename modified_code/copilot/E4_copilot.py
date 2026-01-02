import ast

# ----------------------------
# Original Copilot logic
# ----------------------------
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

# ----------------------------
# Step 5 wrapper
# ----------------------------
def solve(list1=None, list2=None):
    if list1 is None:
        list1 = [1,3,5]
    if list2 is None:
        list2 = [2,4,6]
    l1 = build_list(list1)
    l2 = build_list(list2)
    merged = merge_two_lists(l1, l2)
    out = []
    cur = merged
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

if __name__ == "__main__":
    result = solve()
    print("Merged list (Copilot):", result)  # Expected: [1,2,3,4,5,6]
