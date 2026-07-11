class Solution:
    def isValid(self, s: str) -> bool:
        openers = ['(', '{', '[']
        closers = [')', '}', ']']
        stack = []
        for c in s:
            if c in closers:
                if len(stack) == 0:
                    return False
                elif openers[closers.index(c)] == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif c in openers:
                stack.append(c)
            
        if len(stack) != 0:
            return False
        else:
            return True