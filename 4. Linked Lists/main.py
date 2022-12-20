class Node:
    def __init__(self, value):
        self._value = value
        self._next = None


class LinkedList(object):
    def __init__(self, head=None):
        self._head = head
        self._tail = None

    def _isEmpty(self):
        if self._head == None:
            return True
        return False

    def addLast(self, item):
        node = Node(item)
        if self._isEmpty():
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node

    def addFirst(self, item):
        node = Node(item)
        if self._isEmpty():
            self._head = node
            self._tail = node
        else:
            node._next = self._head
            self._head = node

    def __str__(self):
        current = self._head
        output = ''
        while current:
            output += str(current._value) + ' '
            current = current._next
        return output


# Test
list = LinkedList()
list.addLast(10)
list.addLast(20)
list.addFirst(40)
list.addLast(30)
print(list)
# Output: 40 10 20 30
