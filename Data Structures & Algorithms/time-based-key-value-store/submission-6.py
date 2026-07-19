class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (self.timemap).get(key) == None:
            self.timemap[key] = [(value, timestamp)]
        else:
            self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # values are stored in asc order
        if self.timemap.get(key) == None:
            return ""
        l = 0 
        h = len(self.timemap[key]) - 1
        closest_index = -1
        while l <= h:
            mid = (l + h) // 2
            print(l)
            print(h)
            print(mid)
            if self.timemap[key][mid][1] == timestamp:
                return self.timemap[key][mid][0]
            elif self.timemap[key][mid][1] < timestamp:
                if closest_index == -1:
                    closest_index = mid
                else:
                    if self.timemap[key][mid][1] > self.timemap[key][closest_index][1]:
                        closest_index = mid
                l = mid + 1
            else:
                h = mid - 1
        if closest_index == -1:
            return ""
        else:
            return self.timemap[key][closest_index][0]
        
