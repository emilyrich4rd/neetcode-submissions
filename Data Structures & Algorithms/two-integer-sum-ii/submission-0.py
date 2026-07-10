class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array of increasing numbers
        # return indices of 2 numbers such that they add up to a target 
        # have to use pointers because we have O(1) space
        # also has to be O(n) time
        l = 0 
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1
            
        