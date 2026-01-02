# ----------------------------
# Original Gemini logic preserved
# ----------------------------
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self) -> Node:
        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = DoublyLinkedList()

    def _move_to_mru(self, node: Node):
        self.list.remove_node(node)
        self.list.add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_mru(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_mru(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.list.add_to_head(new_node)
            if len(self.cache) > self.capacity:
                lru_node = self.list.remove_tail()
                del self.cache[lru_node.key]

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve():
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.get(1)
    cache.put(3, 30)
    cache.get(2)
    cache.put(4, 40)
    cache.get(3)
    cache.get(4)
    return cache

if __name__ == '__main__':
    cache = solve()
    print("A2_gemini executed successfully")
