class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # For every day in the list, how many days until a day with higher temperature
        output = [0] * len(temperatures)
        stack = []
        for t in range(len(temperatures)):
            if len(stack) == 0 or stack[-1][1] >= temperatures[t]:
                stack.append((t, temperatures[t]))
            else:
                while len(stack) > 0 and stack[-1][1] < temperatures[t]:
                    item = stack.pop()
                    output[item[0]] = t - item[0]
                stack.append((t, temperatures[t]))
            print(stack)
        return output