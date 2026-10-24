class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = nums[0]
        for r in range(len(nums)):
            if currentSum < 0:
                currentSum = 0 
            currentSum += nums[r]
            maxSum = max(maxSum, currentSum)
        return maxSum


