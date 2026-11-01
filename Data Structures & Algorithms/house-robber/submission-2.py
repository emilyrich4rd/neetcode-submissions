class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        back_2 = nums[0]
        back_1 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max(back_1, back_2 + nums[i])
            back_2 = back_1
            back_1 = temp
        return back_1