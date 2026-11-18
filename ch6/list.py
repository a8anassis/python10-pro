from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)          # O(1), στο πίσω άκρο

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()      # O(1), από το μπροστινό άκρο

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty queue")
        return self._items[0]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)!r})"


def main() -> None:
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)  # Queue([1, 2, 3])

    print(q.dequeue())  # 1
    print(q.peek())     # 2
    print(len(q))       # 2
    print(q)            # Queue([2, 3])


if __name__ == "__main__":
    main()