class Stack:
    def __init__(self, maxLen):
        if maxLen < 0:
            raise ValueError('Некорректная наибольшая длина')
        self.maxLen = maxLen
        self.l = list()

    def push(self, el):
        if len(self.l) >= self.maxLen:
            raise ValueError('Превышается наибольшая длина')
        self.l.append(el)

    def pop(self):
        return self.l.pop()

    def top(self):
        if len(self.l) == 0:
            return None
        return self.l[len(self.l) - 1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

    def __str__(self):
        return str(self.l)
