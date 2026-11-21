import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for n in range(len(nums)):
            nums[n] *= -1
        heapq.heapify(nums)
        for i in range(k):
            num = heapq.heappop(nums)
        return num * -1