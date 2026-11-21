class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []

        def backtrack(candidate):
            print(candidate)
            if len(candidate) == n:
                res.append(candidate[:])
                return 
            for num in nums:
                if num not in candidate:
                    candidate.append(num)
                    backtrack(candidate)
                    candidate.pop() 
            return

        backtrack([])
        return res