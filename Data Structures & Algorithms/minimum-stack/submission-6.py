class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2**31 - 1
        self.minStack = [self.min]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min:
            self.min = val
            self.minStack.append(val)
        
    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.minStack[-1]:
            self.minStack.pop()
            self.min = self.minStack[-1]
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min 
