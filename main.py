class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
```

Klassni ishlatish uchun misol:

```python
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.size())  # 3
print(q.peek())  # 1
print(q.dequeue())  # 1
print(q.size())  # 2
