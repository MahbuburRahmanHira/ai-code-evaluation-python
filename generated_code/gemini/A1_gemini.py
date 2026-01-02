from typing import Optional, List
from collections import deque

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve():
    """
    Returns the serialize and deserialize functions for a binary tree.
    Uses Level-Order Traversal (BFS) for serialization and deserialization 
    to handle the tree structure efficiently.
    """
    
    # Placeholder for null values in the string representation
    NULL_MARKER = '#'
    # Delimiter to separate node values in the string
    DELIMITER = ','

    def serialize(root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string using BFS (Level-Order Traversal).
        """
        if not root:
            return ""

        # Use a deque for BFS
        queue = deque([root])
        result: List[str] = []

        while queue:
            node = queue.popleft()

            if node:
                # Append the node's value
                result.append(str(node.val))
                
                # Enqueue children, even if they are None, to preserve the structure
                queue.append(node.left)
                queue.append(node.right)
            else:
                # Append the marker for null nodes
                result.append(NULL_MARKER)

        # Join the list of strings with the delimiter
        # The list may end with unnecessary 'None' markers due to the nature of BFS,
        # but the reconstruction handles this. We can remove trailing markers for a cleaner string.
        while result and result[-1] == NULL_MARKER:
            result.pop()
            
        return DELIMITER.join(result)


    def deserialize(data: str) -> Optional[TreeNode]:
        """
        Decodes the encoded string back to a tree.
        """
        if not data:
            return None

        # Split the string by the delimiter to get the list of values/markers
        values = data.split(DELIMITER)
        if not values:
            return None
        
        # The first element is the root
        root = TreeNode(int(values[0]))
        
        # Use a queue for rebuilding the tree in level order
        queue = deque([root])
        i = 1 # Start index for processing values

        while queue and i < len(values):
            parent = queue.popleft()

            # Process left child
            if i < len(values):
                val_left = values[i]
                if val_left != NULL_MARKER:
                    parent.left = TreeNode(int(val_left))
                    queue.append(parent.left)
                i += 1

            # Process right child
            if i < len(values):
                val_right = values[i]
                if val_right != NULL_MARKER:
                    parent.right = TreeNode(int(val_right))
                    queue.append(parent.right)
                i += 1

        return root

    return serialize, deserialize

if __name__ == '__main__':
    # Get the serializer and deserializer functions
    serialize_tree, deserialize_tree = solve()

    # --- Helper function for testing ---
    
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
    
    def to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
        """Helper to convert a tree back to a list (for verification)."""
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # Clean up trailing None markers for standard list representation
        while result and result[-1] is None:
            result.pop()
            
        return result

    # Test Case 1
    tree_values_1 = [1, 2, 3, None, None, 4, 5]
    root_1 = create_tree(tree_values_1)
    
    serialized_1 = serialize_tree(root_1)
    deserialized_root_1 = deserialize_tree(serialized_1)
    deserialized_list_1 = to_list(deserialized_root_1)
    
    print(f"Original: {tree_values_1}")
    print(f"Serialized: {serialized_1}")
    print(f"Deserialized: {deserialized_list_1}")
    
    # Test Case 2 (Single node)
    tree_values_2 = [7]
    root_2 = create_tree(tree_values_2)
    serialized_2 = serialize_tree(root_2)
    deserialized_root_2 = deserialize_tree(serialized_2)
    deserialized_list_2 = to_list(deserialized_root_2)
    print(f"Original: {tree_values_2}")
    print(f"Serialized: {serialized_2}")
    print(f"Deserialized: {deserialized_list_2}")

    # Test Case 3 (Empty tree)
    tree_values_3 = []
    root_3 = create_tree(tree_values_3)
    serialized_3 = serialize_tree(root_3)
    deserialized_root_3 = deserialize_tree(serialized_3)
    deserialized_list_3 = to_list(deserialized_root_3)
    print(f"Original: {tree_values_3}")
    print(f"Serialized: {serialized_3}")
    print(f"Deserialized: {deserialized_list_3}")