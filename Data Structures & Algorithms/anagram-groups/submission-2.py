class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            sortedVers = "".join(sorted(string))
            if anagrams.get(sortedVers) == None:
                anagrams[sortedVers] = [string]
            else:
                anagrams[sortedVers].append(string)
        return list(anagrams.values())


    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT