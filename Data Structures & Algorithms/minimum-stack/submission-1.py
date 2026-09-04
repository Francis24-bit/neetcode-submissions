class MinStack:

    #The main challenge is figuring out how to return the minimum value in O(1) time.
    #The idea is to return a value that has already been stored, which means we need another list to keep track of the minimum values.
    #In the minimum-value list, backup[-1], the last element always represents the minimum value at the current stage.
    #Every time we push a new value, we update backup by comparing backup[-1] with the new value and storing the smaller one.
    #Every time we pop a value from the stack, we also remove the corresponding minimum value from backup using backup.pop().

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
