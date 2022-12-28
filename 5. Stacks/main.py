class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def __str__(self):
        return str(self.items)


# Test
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
print(stack)
print(stack.peek())
stack.pop()
print(stack)
# Output: ['A', 'B', 'C']
# Output: C
# Output: ['A', 'B']
