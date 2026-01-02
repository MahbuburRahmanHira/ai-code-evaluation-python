class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists into a single sorted linked list.

    :param l1: The head of the first sorted linked list.
    :param l2: The head of the second sorted linked list.
    :return: The head of the merged sorted linked list.
    """
    
    # Create a dummy node to act as the start of the merged list
    dummy = ListNode(0)
    current = dummy
    
    # Iterate while both lists have nodes
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        
        # Move the current pointer forward
        current = current.next
        
    # Attach the remaining nodes from the non-empty list
    if l1:
        current.next = l1
    elif l2:
        current.next = l2
        
    # The merged list starts at dummy.next
    return dummy.next

if __name__ == '__main__':
    # Helper function to convert list to ListNode
    def list_to_listnode(items):
        if not items:
            return None
        head = ListNode(items[0])
        current = head
        for val in items[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert ListNode to list
    def listnode_to_list(head):
        items = []
        current = head
        while current:
            items.append(current.val)
            current = current.next
        return items

    # Example 1: l1 = [1, 2, 4], l2 = [1, 3, 4]
    l1_ex1 = list_to_listnode([1, 2, 4])
    l2_ex1 = list_to_listnode([1, 3, 4])
    merged_head_ex1 = solve(l1_ex1, l2_ex1)
    # print(f"Example 1 Merged List: {listnode_to_list(merged_head_ex1)}") # Expected: [1, 1, 2, 3, 4, 4]

    # Example 2: l1 = [], l2 = [0]
    l1_ex2 = list_to_listnode([])
    l2_ex2 = list_to_listnode([0])
    merged_head_ex2 = solve(l1_ex2, l2_ex2)
    # print(f"Example 2 Merged List: {listnode_to_list(merged_head_ex2)}") # Expected: [0]

    # Example 3: l1 = [], l2 = []
    l1_ex3 = list_to_listnode([])
    l2_ex3 = list_to_listnode([])
    merged_head_ex3 = solve(l1_ex3, l2_ex3)
    # print(f"Example 3 Merged List: {listnode_to_list(merged_head_ex3)}") # Expected: []