import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        min_heap = []
        for num, freq in freqMap.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            elif freq > min_heap[0][0]:
                heapq.heapreplace(min_heap, (freq, num))
        
        result = []
        print(min_heap)
        for i in min_heap:
            result.append(i[1])
        return result

            
            
        