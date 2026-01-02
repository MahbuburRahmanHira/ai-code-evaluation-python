class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds the two numbers represented by linked lists l1 and l2, 
    where digits are stored in reverse order, and returns the resulting linked list.
    """
    # Dummy head for the resulting list. This simplifies handling the head node.
    dummy_head = ListNode(0)
    
    # Current pointer for the resulting list
    current = dummy_head
    
    # Initialize the carry to 0
    carry = 0
    
    # Iterate until both lists are exhausted and there is no carry
    while l1 is not None or l2 is not None or carry != 0:
        # Get the value of the current node, or 0 if the list is exhausted
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        
        # Calculate the sum of the digits and the old carry
        total_sum = val1 + val2 + carry
        
        # New carry is the tens digit of the sum
        carry = total_sum // 10
        
        # The digit for the new node is the ones digit of the sum
        digit = total_sum % 10
        
        # Create a new node with the calculated digit and append it to the result list
        current.next = ListNode(digit)
        
        # Move the current pointer forward
        current = current.next
        
        # Move the list pointers forward (if they exist)
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
            
    # The result list starts at dummy_head.next
    return dummy_head.next

# --- Helper functions for testing (not part of the required solution) ---

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

if __name__ == '__main__':
    # Test Case 1: (2 -> 4 -> 3) + (5 -> 6 -> 4) = 342 + 465 = 807
    # Result: 7 -> 0 -> 8
    l1_arr = [2, 4, 3]
    l2_arr = [5, 6, 4]
    l1 = list_to_linkedlist(l1_arr)
    l2 = list_to_linkedlist(l2_arr)
    result = solve(l1, l2)
    print(f"Test 1: {l1_arr} + {l2_arr} = {linkedlist_to_list(result)}")

    # Test Case 2: (0) + (0) = 0
    # Result: 0
    l1_arr = [0]
    l2_arr = [0]
    l1 = list_to_linkedlist(l1_arr)
    l2 = list_to_linkedlist(l2_arr)
    result = solve(l1, l2)
    print(f"Test 2: {l1_arr} + {l2_arr} = {linkedlist_to_list(result)}")

    # Test Case 3: (9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9) + (9 -> 9 -> 9 -> 9) = 9999999 + 9999 = 10009998
    # Result: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1
    l1_arr = [9, 9, 9, 9, 9, 9, 9]
    l2_arr = [9, 9, 9, 9]
    l1 = list_to_linkedlist(l1_arr)
    l2 = list_to_linkedlist(l2_arr)
    result = solve(l1, l2)
    print(f"Test 3: {l1_arr} + {l2_arr} = {linkedlist_to_list(result)}")

    # Test Case 4: (1) + (9 -> 9) = 1 + 99 = 100
    # Result: 0 -> 0 -> 1
    l1_arr = [1]
    l2_arr = [9, 9]
    l1 = list_to_linkedlist(l1_arr)
    l2 = list_to_linkedlist(l2_arr)
    result = solve(l1, l2)
    print(f"Test 4: {l1_arr} + {l2_arr} = {linkedlist_to_list(result)}")