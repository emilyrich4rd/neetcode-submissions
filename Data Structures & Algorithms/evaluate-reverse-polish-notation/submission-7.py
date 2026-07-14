import math 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opMap = {"+": self.add, "*": self.multiply, "/": self.divide, "-": self.subtract}
        stack = []
        for tok in tokens:
            operator = opMap.get(tok)
            if operator == None:
                stack.append(int(tok))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(operator(op1, op2))
        return stack[0]

    def add(self, op1, op2):
        return op1 + op2
    
    def subtract(self, op1, op2):
        return op1 - op2
    
    def divide(self, op1, op2):
        return math.trunc(op1 / op2)
    
    def multiply(self, op1, op2):
        return op1 * op2