class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2**31 - 1
        self.minStack = [self.min]

    def push(self, val: int) -> None:
        self.stack.append(val)
        print("added " + str(val))
        if val <= self.min:
            self.min = val
            self.minStack.append(val)
        
    def pop(self) -> None:
        item = self.stack.pop()
# this item may be the minimum in which case we restore to original minimum
# pop is guaranteed to be on non empty stack, but stack may be empty now
        if item == self.minStack[-1]:
            self.minStack.pop()
            self.min = self.minStack[-1]
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min 
