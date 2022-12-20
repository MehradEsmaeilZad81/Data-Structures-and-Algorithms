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

    def indexOf(self, item):
        if not self._isEmpty():
            index = 0
            current = self._head
            while current:
                if current._value == item:
                    return index
                index += 1
                current = current._next
        return -1

    def contains(self, item):
        if not self._isEmpty():
            current = self._head
            while current:
                if current._value == item:
                    return True
                current = current._next
        return False
        # return self.indexOf(item) != -1 !!

    def removeFirst(self):
        if not self._isEmpty():
            if self._head == self._tail:
                self._head = None
                self._tail = None
            else:
                self._head = self._head._next
        else:
            raise RuntimeError()('List is empty')

    def removeLast(self):
        if not self._isEmpty():
            if self._head == self._tail:
                self._head = None
                self._tail = None
            else:
                current = self._head
                while current:
                    if current._next == self._tail:
                        current._next = None
                        self._tail = current
                        break
                    current = current._next
        else:
            raise RuntimeError('List is empty')

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
print(list.indexOf(10))
print(list.contains(20))
list.removeFirst()
print(list)
list.removeLast()
print(list)
# Output: 40 10 20 30
# Output: 1
# Output: True
# Output: 10 20 30
# Output: 10 20
