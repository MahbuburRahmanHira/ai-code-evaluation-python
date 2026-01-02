import threading
from typing import Any, Deque, List
from collections import deque
import timeit
import cProfile

BUFFER_SIZE = 5
ITEMS_COUNT = 20

# ----------------------------
# Original Gemini logic preserved
# ----------------------------
class BoundedBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer: Deque[Any] = deque()
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def produce(self, item: Any):
        with self.lock:
            while len(self.buffer) == self.capacity:
                self.not_full.wait()
            self.buffer.append(item)
            self.not_empty.notify()

    def consume(self) -> Any:
        with self.lock:
            while not self.buffer:
                self.not_empty.wait()
            item = self.buffer.popleft()
            self.not_full.notify()
            return item

class ConditionProducer(threading.Thread):
    def __init__(self, buffer: BoundedBuffer, items_to_produce: int):
        super().__init__()
        self.buffer = buffer
        self.items_to_produce = items_to_produce

    def run(self):
        for i in range(self.items_to_produce):
            self.buffer.produce(f"item-cond-{i}")
        self.buffer.produce(None)

class ConditionConsumer(threading.Thread):
    def __init__(self, buffer: BoundedBuffer):
        super().__init__()
        self.buffer = buffer
        self.consumed_items: List[Any] = []

    def run(self):
        while True:
            item = self.buffer.consume()
            if item is None:
                self.buffer.produce(None)
                break
            self.consumed_items.append(item)

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve() -> int:
    buffer = BoundedBuffer(BUFFER_SIZE)
    
    producer = ConditionProducer(buffer, ITEMS_COUNT)
    consumer1 = ConditionConsumer(buffer)
    consumer2 = ConditionConsumer(buffer)
    
    producer.start()
    consumer1.start()
    consumer2.start()
    
    producer.join()
    consumer1.join()
    consumer2.join()
    
    return len(consumer1.consumed_items) + len(consumer2.consumed_items)

if __name__ == '__main__':
    total_consumed = solve()
    print("A5_gemini total items consumed:", total_consumed)
