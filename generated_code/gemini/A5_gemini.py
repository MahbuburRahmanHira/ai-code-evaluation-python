import threading
import time
from typing import Any, Deque
from collections import deque

# --- Alternative solution using Lock and Condition Variables ---

class BoundedBuffer:
    """
    Implements a bounded buffer using a deque, lock, and condition variables.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer: Deque[Any] = deque()
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def produce(self, item: Any):
        """Adds an item to the buffer."""
        with self.lock:
            while len(self.buffer) == self.capacity:
                # Wait until buffer is not full
                self.not_full.wait()
            
            self.buffer.append(item)
            # Notify waiting consumers
            self.not_empty.notify()

    def consume(self) -> Any:
        """Removes and returns an item from the buffer."""
        with self.lock:
            while not self.buffer:
                # Wait until buffer is not empty
                self.not_empty.wait()
            
            item = self.buffer.popleft()
            # Notify waiting producers
            self.not_full.notify()
            
            return item

class ConditionProducer(threading.Thread):
    def __init__(self, buffer: BoundedBuffer, items_to_produce: int):
        super().__init__()
        self.buffer = buffer
        self.items_to_produce = items_to_produce

    def run(self):
        for i in range(self.items_to_produce):
            item = f"item-cond-{i}"
            self.buffer.produce(item)
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

def solve_condition_based():
    """
    Alternative solve function using the Lock/Condition implementation.
    """
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

# The primary solve() must return the one expected implementation (queue.Queue is standard)
def solve_primary():
    return solve()

# NOTE: Since the instruction requests one code, I'll prioritize the queue.Queue implementation.
# The code blocks provided above are for the two common Python solutions.