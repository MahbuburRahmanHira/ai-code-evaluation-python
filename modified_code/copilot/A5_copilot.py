import threading
import queue
import time
import random

# ----------------------------
# Original Copilot logic preserved
# ----------------------------
def producer(q: queue.Queue, producer_id: int, items: int, delay: tuple):
    for i in range(items):
        item = (producer_id, i)
        q.put(item)
        time.sleep(random.uniform(*delay))

def consumer(q: queue.Queue, consumer_id: int, delay: tuple):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        time.sleep(random.uniform(*delay))
        q.task_done()

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve():
    capacity = 5
    n_producers = 3
    n_consumers = 2
    items_per_producer = 10
    prod_delay = (0.01, 0.06)
    cons_delay = (0.02, 0.08)

    q = queue.Queue(maxsize=capacity)

    producers = []
    consumers = []

    for cid in range(n_consumers):
        t = threading.Thread(target=consumer, args=(q, cid, cons_delay), daemon=True)
        t.start()
        consumers.append(t)

    for pid in range(n_producers):
        t = threading.Thread(target=producer, args=(q, pid, items_per_producer, prod_delay), daemon=True)
        t.start()
        producers.append(t)

    for t in producers:
        t.join()

    for _ in range(n_consumers):
        q.put(None)

    q.join()
    for t in consumers:
        t.join()

    return n_producers * items_per_producer

if __name__ == "__main__":
    total_items = solve()
    print("A5_copilot total items produced and consumed:", total_items)
