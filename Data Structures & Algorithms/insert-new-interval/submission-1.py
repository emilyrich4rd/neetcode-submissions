class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find the position and then merge
        def mergeIntervals(int1, int2):
            return [min(int1[0], int2[0]), max(int1[1], int2[1])]

        position = 0 
        posFound = False
        for i in range(len(intervals)):
            curr = intervals[i]
            # either should be in this position or has to be merged
            if curr[0] > newInterval[1]:
                intervals.insert(i, newInterval)
                return intervals
            elif newInterval[0] > curr[1]:
                continue # position not here 
            else:
                # either new interval is inside our current one or it exceeds that
                # if it exceeds we merge and break to keep merging until no more overlap
                # easier to merge them then just look for overlap
                mergedInterval = mergeIntervals(newInterval, curr)
                intervals[i] = mergedInterval 
                position = i 
                posFound = True
                break   
        if not posFound:
            intervals.append(newInterval)
            return intervals
        while position < len(intervals)-1 and intervals[position][1] >= intervals[position+1][0]:
            intervals[position] = mergeIntervals(intervals[position], intervals[position+1])
            intervals.pop(position+1)
        return intervals

