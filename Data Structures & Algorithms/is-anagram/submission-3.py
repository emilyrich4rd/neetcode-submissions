class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sortS = sorted(s)
        sortT = sorted(t)
        return sortS == sortT
