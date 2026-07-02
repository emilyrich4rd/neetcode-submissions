class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        buckets = [[]] * len(nums)
        for num, freq in freqMap.items():
            if buckets[freq-1] == []:
                buckets[freq-1] = [num]
            else:
                buckets[freq-1].append(num)
        lst = []
        for i in range(len(buckets)):
            lst.extend(buckets[i])
        return lst[len(lst)-k:]