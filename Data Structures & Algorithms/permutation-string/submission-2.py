class Solution:

    def compareStrings(self, s1, s2):
        dict1 = {}
        dict2 = {}
    
        for c in s2:
            if dict2.get(c) == None:
                dict2[c] = 1
            else:
                dict2[c] += 1
        return dict1 == dict2
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        for c in s1:
            if dict1.get(c) == None:
                dict1[c] = 1
            else:
                dict1[c] += 1
        ptr1 = 0
        ptr2 = len(s1)
        while ptr2 <= len(s2):
            print(s2[ptr1:ptr2])
            dict2 = {}
            for c in s2[ptr1:ptr2]:
                if dict2.get(c) == None:
                    dict2[c] = 1
                else:
                    dict2[c] += 1
            if dict1 == dict2:
                return True
            else:
                ptr2 += 1
                ptr1 += 1
        return False