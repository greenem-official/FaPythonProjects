class LinkedListNode:
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

class LinkedList:
    firstEl = None

    def add(self, value):
        if not self.firstEl:
            self.firstEl = LinkedListNode(value)
        else:
            node = self.firstEl
            while node.getNext():
                node = node.getNext()
            node.setNext(LinkedListNode(value))

    def remove(self, value):
        if not self.firstEl:
            raise ValueError('Список пуст')
        else:
            if self.firstEl.getValue() == value:
                self.__removeSingle(self.firstEl)
                self.firstEl = None
                return
            node = self.firstEl
            while node.getNext():
                if node.getNext().getValue() == value:
                    self.__removeSingle(node)
                    return
        raise ValueError('Нет такого элемента')

    def __removeSince(self, el: LinkedListNode):
        if not el:
            return
        self.__removeSince(el.getNext())
        el.setNext(None)

    def __removeSingle(self, el: LinkedListNode):
        toRemove = el.getNext()
        nextAfterIt = None
        if toRemove:
            nextAfterIt = toRemove.getNext()
        el.setNext(nextAfterIt)

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