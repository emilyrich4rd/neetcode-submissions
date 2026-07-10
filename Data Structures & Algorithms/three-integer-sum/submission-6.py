class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ordered = sorted(nums)
        triplets = set()
        for i, n in enumerate(ordered):
            if n > 0:
                break
            l = i+1
            r = len(ordered) - 1
            while l < r:
                if ordered[l] + ordered[r] + n == 0 and i != l and i != r:
                    t = sorted((ordered[l], ordered[r], n))
                    triplets.add(tuple(t))
                    l += 1
                    r -= 1
                elif ordered[l] + ordered[r] + n < 0:
                    l += 1
                else:
                    r -= 1
        return list(triplets)