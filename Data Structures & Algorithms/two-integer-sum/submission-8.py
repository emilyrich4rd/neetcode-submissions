class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = [(nums[i], target - nums[i]) for i in range (len(nums))]
        for pair in pairs:
            if nums.count(pair[0]) != 0 and nums.count(pair[1]) != 0:
                pos1 = nums.index(pair[0])
                if pair[1] in nums[pos1+1:]:
                    pos2 = nums.index(pair[1], pos1 + 1)
                    return [pos1, pos2]
