import threading
import queue
import time
import random
import sys

def producer(q: queue.Queue, producer_id: int, items: int, delay: tuple):
    for i in range(items):
        item = (producer_id, i)
        # block if queue is full
        q.put(item)
        print(f"[Producer {producer_id}] produced {item} (queue_size={q.qsize()})", flush=True)
        time.sleep(random.uniform(*delay))
    print(f"[Producer {producer_id}] finished producing.", flush=True)

def consumer(q: queue.Queue, consumer_id: int, delay: tuple):
    while True:
        item = q.get()
        try:
            # Sentinel to stop
            if item is None:
                print(f"[Consumer {consumer_id}] received stop signal.", flush=True)
                q.task_done()
                break
            # process item
            print(f"[Consumer {consumer_id}] consumed {item} (queue_size={q.qsize()})", flush=True)
            time.sleep(random.uniform(*delay))
            q.task_done()
        except Exception as e:
            # ensure task_done called on exception to avoid deadlock
            try:
                q.task_done()
            except Exception:
                pass
            print(f"[Consumer {consumer_id}] error: {e}", flush=True)
            break
    print(f"[Consumer {consumer_id}] exiting.", flush=True)

def solve():
    # Configuration (reasonable defaults)
    capacity = 5
    n_producers = 3
    n_consumers = 2
    items_per_producer = 10
    prod_delay = (0.01, 0.06)
    cons_delay = (0.02, 0.08)

    # Edge-case handling
    try:
        capacity = int(capacity)
    except Exception:
        capacity = 1
    if capacity <= 0:
        capacity = 1
    if n_producers <= 0:
        n_producers = 1
    if n_consumers <= 0:
        n_consumers = 1
    if items_per_producer < 0:
        items_per_producer = 0

    q = queue.Queue(maxsize=capacity)

    producers = []
    consumers = []

    # Start consumer threads first (they will block waiting on queue)
    for cid in range(n_consumers):
        t = threading.Thread(target=consumer, args=(q, cid, cons_delay), daemon=True)
        t.start()
        consumers.append(t)

    # Start producer threads
    for pid in range(n_producers):
        t = threading.Thread(target=producer, args=(q, pid, items_per_producer, prod_delay), daemon=True)
        t.start()
        producers.append(t)

    try:
        # Wait for all producers to finish
        for t in producers:
            t.join()

        # After producers finish, send stop signals (one per consumer)
        for _ in range(n_consumers):
            q.put(None)

        # Wait until all produced items have been processed
        q.join()

        # Wait for consumers to exit
        for t in consumers:
            t.join()
    except KeyboardInterrupt:
        print("Interrupted. Attempting graceful shutdown...", flush=True)
        # Best-effort shutdown: send stop signals
        for _ in range(n_consumers):
            try:
                q.put_nowait(None)
            except Exception:
                pass

    print("All producers and consumers have exited.", flush=True)

if __name__ == "__main__":
    solve()