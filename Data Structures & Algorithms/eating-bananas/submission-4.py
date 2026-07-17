import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = 0
        for num in piles:
            if num > max_k:
                max_k = num
        l = 1
        u = max_k
        min_k = max_k
        # success condition is ceil(x/k) summed for every x (pile number)
        while l <= u:
            mid = (l + u) // 2
            sum = 0 
            for num in piles:
                sum += math.ceil(num / mid)
            
            # print(f"Total hours({mid}) = {sum}") 
            if sum <= h:
                min_k = min(min_k, mid)
                u = mid - 1
            else:
                l = mid + 1
        return min_k




        