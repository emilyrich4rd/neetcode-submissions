class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diffs.get(diff) == None:
                diffs[nums[i]] = i
            else:
                return [diffs[diff], i]
        return []   