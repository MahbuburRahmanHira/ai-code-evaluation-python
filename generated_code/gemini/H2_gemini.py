from typing import List, Optional
import heapq

class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists into one sorted list using a min-heap.
    
    The min-heap stores the current smallest node from each of the k lists.
    The time complexity is O(N log k), where N is the total number of nodes 
    and k is the number of linked lists.
    """
    # Min-heap to store the head of the lists
    min_heap = []
    
    # Push the head node of each non-empty list into the min-heap
    for i, head in enumerate(lists):
        if head:
            # The heapq module can only compare elements that are directly comparable.
            # When storing objects (ListNode), it compares them based on their first element.
            # To handle cases where two nodes might have the same value, we use a tuple:
            # (node.val, index, node). The index (i) breaks ties and prevents comparison errors
            # between ListNode objects themselves (which don't support the < operator).
            heapq.heappush(min_heap, (head.val, i, head))
            
    # Dummy head for the resulting merged list
    dummy_head = ListNode(0)
    current = dummy_head
    
    # Process nodes until the min-heap is empty
    while min_heap:
        # Extract the smallest node (k-th smallest element) from the heap
        val, i, smallest_node = heapq.heappop(min_heap)
        
        # Append the smallest node to the merged list
        current.next = smallest_node
        current = current.next
        
        # If the extracted node has a next node, push the next node onto the heap
        if smallest_node.next:
            # Note: We must use a new index for the tie-breaker since the previous one is associated 
            # with the list it came from, but for simplicity and safety against node comparison issues,
            # we can reuse the list index 'i' as the tie-breaker for all subsequent nodes from that list.
            # Python's heapq is usually fine with tuples of the same length, where it compares 
            # the first element, then the second, and so on. Since the list index 'i' is unique 
            # per list, it's a good tie-breaker.
            heapq.heappush(min_heap, (smallest_node.next.val, i, smallest_node.next))
            
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
    # Test Case 1: Example from problem description
    # List 1: 1 -> 4 -> 5
    # List 2: 1 -> 3 -> 4
    # List 3: 2 -> 6
    list_arrs = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [list_to_linkedlist(arr) for arr in list_arrs]
    
    result = solve(lists)
    result_list = linkedlist_to_list(result)
    # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
    print(f"Input: {list_arrs}, Output: {result_list}")

    # Test Case 2: Empty list of lists
    list_arrs_2 = []
    lists_2 = [list_to_linkedlist(arr) for arr in list_arrs_2]
    result_2 = solve(lists_2)
    result_list_2 = linkedlist_to_list(result_2)
    print(f"Input: {list_arrs_2}, Output: {result_list_2}")

    # Test Case 3: List containing an empty list
    list_arrs_3 = [[], [0]]
    lists_3 = [list_to_linkedlist(arr) for arr in list_arrs_3]
    result_3 = solve(lists_3)
    result_list_3 = linkedlist_to_list(result_3)
    # Expected: 0
    print(f"Input: {list_arrs_3}, Output: {result_list_3}")