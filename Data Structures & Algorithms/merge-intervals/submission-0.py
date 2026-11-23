class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        def mergeIntervals(x, y):
            return [min(x[0], y[0]), max(x[1], y[1])]

        i = 0 
        while i < len(intervals)-1:
            i1 = intervals[i]
            i2 = intervals[i+1]
            if i1[1] >= i2[0]:
                intervals[i] = mergeIntervals(i1, i2)
                intervals.pop(i+1)
            else:
                i += 1
        return intervals

