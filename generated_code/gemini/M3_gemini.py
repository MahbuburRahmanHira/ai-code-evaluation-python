from collections import deque
from typing import List, Optional

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Performs a level-order traversal (Breadth-First Search) on a binary tree.
    Returns the traversal as a list of lists, where each inner list contains 
    the node values at that level.
    """
    if root is None:
        return []

    # Initialize a deque (double-ended queue) for the BFS queue, 
    # starting with the root node.
    queue = deque([root])
    
    # List to store the results (list of lists)
    result = []

    # Loop as long as there are nodes to process in the queue
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        
        # List to store the values of the nodes at the current level
        current_level_nodes = []

        # Process all nodes currently in the queue (i.e., all nodes at the current level)
        for _ in range(level_size):
            # Dequeue the node at the front
            node = queue.popleft()
            
            # Add the node's value to the current level list
            current_level_nodes.append(node.val)

            # Enqueue the left child, if it exists
            if node.left:
                queue.append(node.left)
            
            # Enqueue the right child, if it exists
            if node.right:
                queue.append(node.right)

        # After processing all nodes at this level, add the level list to the result
        result.append(current_level_nodes)

    return result

# --- Helper functions for testing (not part of the required solution) ---

def create_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper to create a binary tree from a list (level-order representation)."""
    if not values:
        return None
    
    # Use a queue for building the tree in level order
    nodes = [None if val is None else TreeNode(val) for val in values]
    root = nodes[0]
    
    parent_index = 0
    for i in range(1, len(nodes), 2):
        parent = nodes[parent_index]
        if parent:
            # Left child
            if i < len(nodes):
                parent.left = nodes[i]
            # Right child
            if i + 1 < len(nodes):
                parent.right = nodes[i + 1]
        
        parent_index += 1
        
    return root

if __name__ == '__main__':
    # Test Case 1: [3, 9, 20, None, None, 15, 7]
    # Expected Output: [[3], [9, 20], [15, 7]]
    tree_values_1 = [3, 9, 20, None, None, 15, 7]
    root_1 = create_tree(tree_values_1)
    print(f"Input: {tree_values_1}, Output: {solve(root_1)}")

    # Test Case 2: [1]
    # Expected Output: [[1]]
    tree_values_2 = [1]
    root_2 = create_tree(tree_values_2)
    print(f"Input: {tree_values_2}, Output: {solve(root_2)}")
    
    # Test Case 3: [] (Edge Case)
    # Expected Output: []
    tree_values_3 = []
    root_3 = create_tree(tree_values_3)
    print(f"Input: {tree_values_3}, Output: {solve(root_3)}")

    # Test Case 4: [1, 2, 3, 4, None, None, 5]
    # Expected Output: [[1], [2, 3], [4, 5]]
    tree_values_4 = [1, 2, 3, 4, None, None, 5]
    root_4 = create_tree(tree_values_4)
    print(f"Input: {tree_values_4}, Output: {solve(root_4)}")