class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i, n in enumerate(nums):
            if n > 0:
                break
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + n == 0 and i != l and i != r:
                    t = sorted((nums[l], nums[r], n))
                    triplets.add(tuple(t))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + n < 0:
                    l += 1
                else:
                    r -= 1
        return list(triplets)