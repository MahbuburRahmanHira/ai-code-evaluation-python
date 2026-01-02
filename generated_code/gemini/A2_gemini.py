class Node:
    """
    A doubly linked list node. Stores key and value for easy removal from hashmap 
    and fast list operations.
    """
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """
    A simple Doubly Linked List for tracking the order of usage.
    Head is the sentinel node for MRU, Tail is the sentinel node for LRU.
    """
    def __init__(self):
        # Head (MRU end) and Tail (LRU end) are sentinel nodes for simpler code
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node: Node):
        """Adds a new node right after the head (MRU side)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        """Removes a node from its current position."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self) -> Node:
        """Removes and returns the LRU node (node before the tail)."""
        if self.tail.prev == self.head:
            # Should not happen in a correctly implemented cache
            raise Exception("Cannot remove from empty list")
        
        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node

class LRUCache:
    """
    Implements a Least Recently Used (LRU) Cache using a hash map and a doubly linked list.
    
    - Hash Map (self.cache): Stores key -> Node mapping for O(1) access.
    - Doubly Linked List (self.list): Stores Node objects in order of usage.
      - Head -> ... MRU ... -> LRU ... -> Tail
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Hash map: key -> Node object
        self.cache = {}
        # Doubly Linked List
        self.list = DoublyLinkedList()

    def _move_to_mru(self, node: Node):
        """Removes the node and re-adds it to the head of the list."""
        self.list.remove_node(node)
        self.list.add_to_head(node)

    def get(self, key: int) -> int:
        """
        Retrieves the value of the key in O(1).
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Mark as most recently used
        self._move_to_mru(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Updates or inserts the key-value pair in O(1).
        Handles capacity eviction.
        """
        if key in self.cache:
            # Update existing: change value and move to MRU
            node = self.cache[key]
            node.value = value
            self._move_to_mru(node)
        else:
            # Insert new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.list.add_to_head(new_node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                # Evict LRU item (node before the tail)
                lru_node = self.list.remove_tail()
                # Remove from hash map
                del self.cache[lru_node.key]

def solve(capacity: int) -> LRUCache:
    """
    Factory function to return an LRUCache object.
    (Returns the Doubly Linked List based implementation which is the classical solution).
    """
    return LRUCache(capacity)