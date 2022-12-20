class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

class LinkedList(object):
    def __init__(self, head = None):
        self._head = head
        self._tail = None