class Solution:
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = defaultdict(int)
        for c in s1:
            if dict1.get(c) == None:
                dict1[c] = 1
            else:
                dict1[c] += 1
        ptr1 = 0
        ptr2 = len(s1)

        # initially set up the dictionary
        dict2 = defaultdict(int)
        for c in s2[ptr1:ptr2]:
            dict2[c] += 1

        while ptr2 <= len(s2):
            print(dict2, dict1)
            print(ptr1, ptr2)
            if dict1 == dict2:
                return True
            else:
                # inclusive ptr2, so need to remove ptr1 from count, increment ptr2 then add it
                dict2[s2[ptr1]] -= 1
                if dict2[s2[ptr1]] == 0:
                    dict2.pop(s2[ptr1])
                if ptr2 != len(s2):
                    dict2[s2[ptr2]] += 1
                ptr1 += 1
                ptr2 += 1
        return False