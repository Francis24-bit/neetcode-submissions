class MinStack:

    def __init__(self):
        self.book = []
        self.backup = []

    def push(self, val: int) -> None:
        self.book.append(val)
        if not self.backup:
            self.backup.append(val)
        else:
            self.backup.append(min(self.backup[-1], val))

    def pop(self) -> None:
        self.book.pop()
        self.backup.pop()

    def top(self) -> int:
        return self.book[-1]

    def getMin(self) -> int:
        return self.backup[-1]
