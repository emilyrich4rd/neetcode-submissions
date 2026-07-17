class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        h = len(nums)-1
        res = nums[0]
        while l <= h:
            if nums[l] < nums[h]: # the whole section is sorted, but nums[l] may be lowest
                res = min(res, nums[l])
                return res

            mid = (l + h) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1 # not sorted and low and mid are same, then must be the num after
            else:
                h = mid - 1 # we accounted for mid being equal so can do mid - 1
        return res
                


