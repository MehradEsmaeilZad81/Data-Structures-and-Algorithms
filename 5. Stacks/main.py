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


def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string


# Test
print(reverse_string("I Love Mercedes"))
# Output: sedarbeM evoL I


# Test
# stack = Stack()
# stack.push("A")
# stack.push("B")
# stack.push("C")
# print(stack)
# print(stack.peek())
# stack.pop()
# print(stack)
# Output: ['A', 'B', 'C']
# Output: C
# Output: ['A', 'B']
