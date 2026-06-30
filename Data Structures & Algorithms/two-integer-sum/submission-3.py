class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ptr1 = 0 
        ptr2 = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
            