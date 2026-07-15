class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        h = len(nums)-1
        while l <= h:
            mid = (l + h) // 2
            print(f"{l} // {h} = {mid}")
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return -1 