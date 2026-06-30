class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []
        for str1 in strs:
            current = []
            for str2 in strs:
                if self.isAnagram(str1, str2):
                    current.append(str2)
            if not (current in anagram_list):
                anagram_list.append(current)
        return anagram_list


    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT