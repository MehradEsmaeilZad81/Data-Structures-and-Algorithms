class Node:
    def __init__(self, value=None):
        self._value = value
        self._next = None


class LinkedList(object):
    def __init__(self, head=None):
        self._head = head
        self._tail = None
        self._size = 0

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
        self._size += 1

    def addFirst(self, item):
        node = Node(item)
        if self._isEmpty():
            self._head = node
            self._tail = node
        else:
            node._next = self._head
            self._head = node
        self._size += 1

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
            self._size -= 1
        else:
            raise RuntimeError('List is empty')

    def _getPrevious(self, node):
        current = self._head
        while current:
            if current._next == node:
                return current
            current = current._next

    def removeLast(self):
        if not self._isEmpty():
            if self._head == self._tail:
                self._head = None
                self._tail = None
            else:
                previous = self._getPrevious(self._tail)
                self._tail = previous
                self._tail._next = None
            self._size -= 1
        else:
            raise RuntimeError('List is empty')

    def size(self):
        return self._size

    def reverse(self):
        if not self._isEmpty():
            previous = self._head
            current = self._head._next
            while current:
                next = current._next
                current._next = previous
                previous = current
                current = next

            self._tail = self._head
            self._tail._next = None
            self._head = previous

    def getKthFromTheEnd(self, k):
        if not self._isEmpty():
            a = self._head
            b = self._head
            for i in range(k):
                b = b._next
                if b == None:
                    raise RuntimeError(
                        'k is greater than the size of the list')
            while b:
                a = a._next
                b = b._next
            return a._value
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
print(list.getKthFromTheEnd(2))
print(list)
list.reverse()
print(list)
print(list.indexOf(10))
print(list.contains(20))
print('size:', list.size())
list.removeFirst()
print(list)
list.reverse()
list.removeLast()
print('size:', list.size())
print(list)

# Output:
# 20
# 40 10 20 30
# 30 20 10 40
# 2
# True
# size: 4
# 20 10 40
# size: 2
# 40 10
