class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(result, candidate, i):
            if len(candidate) == len(nums):
                result.append(candidate)
                return 
            for n in range(i, len(nums)):
                candidate.append(nums[n])
                result.append(candidate.copy())
                helper(result, candidate, n + 1)
                candidate.pop() 
            return  
        res = []
        helper(res, [], 0)
        return res