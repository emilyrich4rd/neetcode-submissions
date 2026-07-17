class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        h = len(nums)-1
        res = nums[0]
        while l <= h:
            if nums[l] < nums[h]:
                res = min(res, nums[l])
                return res

            mid = (l + h) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1 # obviously nums[mid] is bigger so we can't have = mid 
            else:
                h = mid - 1 # but if it is less we can't say anything of the mid
        return res
                


