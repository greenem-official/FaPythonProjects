class LinkedQueueNode:
    value: any
    nextEl = None

    def __init__(self, value):
        self.value = value

    def setNext(self, nextEl):
        self.nextEl = nextEl

    def getNext(self):
        return self.nextEl

    def getValue(self):
        return self.value


class LinkedQueue:
    firstEl = None

    def append(self, value):
        if not self.firstEl:
            self.firstEl = LinkedQueueNode(value)
        else:
            node = self.firstEl
            while node.getNext():
                node = node.getNext()
            node.setNext(LinkedQueueNode(value))

    def pop(self):
        if not self.firstEl:
            return None
        node = self.firstEl
        while node.getNext() and node.getNext().getNext():
            node = node.getNext()
        res = node.getNext()
        node.setNext(None)
        return res.getValue()

    def get(self):
        if not self.firstEl:
            return None
        node = self.firstEl
        while node.getNext():
            node = node.getNext()
        return node.getValue()

    def find(self, value):
        if not self.firstEl:
            return None
        else:
            c = 0
            node = self.firstEl
            while node.getNext():
                if node.getValue() == value:
                    return c, node
                node = node.getNext()
                c += 1

    def count(self, value):
        if not self.firstEl:
            return 0
        else:
            c = 0
            node = self.firstEl
            if node.getValue() == value:
                c += 1
            while node.getNext():
                node = node.getNext()
                if node.getValue() == value:
                    c += 1
            return c

    def __str__(self):
        s = None
        node = self.firstEl
        if node:
            s = ''
            while node:
                s += node.getValue() + ' '
                node = node.getNext()
            s = s[:len(s)-1]
        return s
