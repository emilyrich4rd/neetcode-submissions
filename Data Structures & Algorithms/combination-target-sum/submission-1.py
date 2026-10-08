class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        end = len(nums)
        
        def helper(i, currentList, currSum):
            if currSum == target:
                result.append(currentList.copy())
                return
        
            for n in range(i, end):
                total = currSum + nums[n]
                if total > target:
                    return
                currentList.append(nums[n])
                helper(n, currentList, total)
                currentList.pop()
                

        helper(0, [], 0)
        return result
