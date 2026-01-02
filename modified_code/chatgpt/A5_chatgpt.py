import threading
import time
import random
from collections import deque

# ----------------------------
# Original ChatGPT logic preserved
# ----------------------------
class BoundedBuffer:
    def __init__(self, capacity):
        self.buffer = deque()
        self.capacity = capacity
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    def put(self, item):
        with self.not_full:
            while len(self.buffer) >= self.capacity:
                self.not_full.wait()
            self.buffer.append(item)
            self.not_empty.notify()

    def get(self):
        with self.not_empty:
            while not self.buffer:
                self.not_empty.wait()
            item = self.buffer.popleft()
            self.not_full.notify()
            return item

def producer(buffer, items):
    for item in items:
        buffer.put(item)
        time.sleep(random.uniform(0.01, 0.1))

def consumer(buffer, consume_count):
    for _ in range(consume_count):
        buffer.get()
        time.sleep(random.uniform(0.01, 0.1))

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve():
    buffer = BoundedBuffer(capacity=5)
    items_to_produce = list(range(20))
    prod_thread = threading.Thread(target=producer, args=(buffer, items_to_produce))
    cons_thread = threading.Thread(target=consumer, args=(buffer, len(items_to_produce)))

    prod_thread.start()
    cons_thread.start()
    prod_thread.join()
    cons_thread.join()

    # Return final buffer state for verification
    return list(buffer.buffer)

if __name__ == "__main__":
    result = solve()
    print("A5_chatgpt final buffer state:", result)
