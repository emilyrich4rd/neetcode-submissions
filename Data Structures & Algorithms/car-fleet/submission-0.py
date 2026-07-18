class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [] 
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        stack = []
        for (pos, s) in cars:
            time = (target - pos) / s 
            if len(stack) == 0:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)
                    
