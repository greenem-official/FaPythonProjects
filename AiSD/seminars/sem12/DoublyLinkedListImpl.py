class DoublyLinkedListNode:
    value: any
    nextEl = None
    prevEl = None

    def __init__(self, value):
        self.value = value

    def setNext(self, nextEl):
        self.nextEl = nextEl

    def setPrev(self, prevEl):
        self.prevEl = prevEl

    def getNext(self):
        return self.nextEl

    def getPrev(self):
        return self.prevEl

    def getValue(self):
        return self.value


class DoublyLinkedList:
    firstEl = None
    lastEl = None

    def addToEnd(self, value):
        if not self.firstEl:
            self.firstEl = DoublyLinkedListNode(value)
            self.lastEl = self.firstEl
        else:
            node = self.firstEl
            while node.getNext():
                node = node.getNext()
            newNode = DoublyLinkedListNode(value)
            node.setNext(newNode)
            newNode.setPrev(node)
            self.lastEl = newNode

    def addToBeginning(self, value):
        if not self.lastEl:
            self.lastEl = DoublyLinkedListNode(value)
        else:
            node = self.lastEl
            while node.getPrev():
                node = node.getPrev()
            newNode = DoublyLinkedListNode(value)
            node.setPrev(newNode)
            newNode.setNext(node)
            self.firstEl = newNode

    def getFirst(self):
        return self.firstEl.getValue() if self.firstEl else None

    def getLast(self):
        return self.lastEl.getValue() if self.lastEl else None

    def popFirst(self):
        if self.firstEl:
            oldFirst = self.firstEl
            node = self.firstEl.getNext()
            if node:
                node.setPrev(None)
                self.firstEl.setNext(None)
                self.firstEl = node
            else:
                self.firstEl = None
            return oldFirst.getValue()

    def popLast(self):
        if self.lastEl:
            oldLast = self.lastEl
            node = self.lastEl.getPrev()
            if node:
                node.setNext(None)
                self.lastEl.setPrev(None)
                self.lastEl = node
            else:
                self.lastEl = None
            return oldLast.getValue()

    def get(self, index):
        if not self.firstEl:
            raise IndexError('Индекс вне границ списка')
        else:
            node = self.firstEl
            for i in range(index):
                if node.getNext():
                    node = node.getNext()
                else:
                    raise IndexError('Индекс вне границ списка')
            return node.getValue()


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

    def __removeSince(self, el: DoublyLinkedListNode):
        if not el:
            return
        self.__removeSince(el.getNext())
        if el.getNext():
            el.getNext().setPrev(None)
        el.setNext(None)

    def __removeSingle(self, el: DoublyLinkedListNode):
        toRemove = el.getNext()
        nextAfterIt = None
        if toRemove:
            nextAfterIt = toRemove.getNext()
        el.setNext(nextAfterIt)
        if nextAfterIt:
            nextAfterIt.setPrev(el)
        if toRemove:
            toRemove.setNext(None)
            toRemove.setPrev(None)

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
