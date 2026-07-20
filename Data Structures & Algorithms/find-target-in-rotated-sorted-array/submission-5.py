class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        h = len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            print(mid)
            if nums[mid] == target:
                return mid 
            elif nums[l] <= nums[mid]: # low to mid section is sorted
                if target < nums[mid] and target >= nums[l]:
                    h = mid - 1
                else:
                    l = mid + 1
            else: # mid to upper section sorted
                if nums[mid] < target and nums[h] >= target:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1