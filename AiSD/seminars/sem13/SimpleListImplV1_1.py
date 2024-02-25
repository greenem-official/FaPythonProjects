class SimpleListNode:
    value: any
    nextEl = None

    def __init__(self, value):
        self.value = value


class SimpleList:
    firstEl = None

    def append(self, value):
        if not self.firstEl:
            self.firstEl = SimpleListNode(value)
        else:
            node = self.firstEl
            while node.nextEl:
                node = node.nextEl
            node.nextEl = SimpleListNode(value)

    def set(self, value, index):
        if not self.firstEl or index == 0:
            newNode = SimpleListNode(value)
            if self.firstEl:
                newNode.nextEl = self.firstEl.nextEl
            self.firstEl = newNode
        else:
            node = self.firstEl
            i = 0
            while node.nextEl and i < index - 1:
                node = node.nextEl
                i += 1
            if i == index - 1:
                newNode = SimpleListNode(value)
                if node.nextEl and node.nextEl.nextEl:
                    newNode.nextEl = node.nextEl.nextEl
                node.nextEl = newNode

    def __getitem__(self, index):
        if not self.firstEl:
            raise KeyError('Список пуст!')
        else:
            node = self.firstEl
            i = 0
            while node.nextEl and i < index:
                node = node.nextEl
                i += 1
            if i == index:
                return node.value
            else:
                raise KeyError('За пределами списка!')

    def __len__(self):
        if not self.firstEl:
            return 0
        else:
            node = self.firstEl
            i = 0
            while node.nextEl:
                node = node.nextEl
                i += 1
            return i

    def remove(self, index):
        if not self.firstEl:
            raise KeyError('Список пуст!')
        elif index == 0:
            if self.firstEl:
                self.firstEl = self.firstEl.nextEl
        else:
            node = self.firstEl
            i = 0
            while node.nextEl and i < index - 1:
                node = node.nextEl
                i += 1
            if i == index - 1:
                if node.nextEl and node.nextEl.nextEl:
                    node.nextEl = node.nextEl.nextEl

    def __removeSingle(self, el: SimpleListNode):
        toRemove = el.nextEl
        nextAfterIt = None
        if toRemove:
            nextAfterIt = toRemove.nextEl
            toRemove.nextEl = None
        el.nextEl = nextAfterIt

    def __str__(self):
        s = None
        node = self.firstEl
        if node:
            s = ''
            while node:
                s += node.value + ' '
                node = node.nextEl
            s = s[:len(s)-1]
        return s
