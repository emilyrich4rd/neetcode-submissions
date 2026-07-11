class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0 
        l = 0 
        r = len(heights)-1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > max:
                max = area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max
