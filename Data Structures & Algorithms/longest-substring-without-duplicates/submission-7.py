class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0 
        l1 = 0
        l2 = 0 
        unique = {}
        while l2 != len(s):
            print(s[l1])
            print(s[l2])
            print(unique)
            # because we aren't resetting the dictionary after l1, make sure the check is after l1
            if unique.get(s[l2]) == None or unique[s[l2]] < l1:
                unique[s[l2]] = l2 
            else:
                print("dup")
                maxlen = max(l2 - l1, maxlen)
                l1 = unique[s[l2]] + 1
                unique[s[l2]] = l2
            l2 += 1
        print(f"final l2 {l2}")
        print(f"final l1 {l1}")
        return max(l2 - l1, maxlen)
