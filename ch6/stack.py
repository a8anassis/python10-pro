"""Implementation of a stack data structure using a list."""

class Stack:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)   # επιτρέπει len(s) και `if s:`

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items!r})"


def main() -> None:
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack size:", stack.size())
    print("Popped item:", stack.pop())
    print("Stack size after pop:", stack.size())

if __name__ == "__main__":
    main()