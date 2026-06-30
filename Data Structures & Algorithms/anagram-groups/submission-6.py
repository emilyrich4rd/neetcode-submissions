class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            
            arrkey = [0] * 26
            for c in string:
                arrkey[ord(c) - ord('a')] += 1
        
            anagrams[tuple(arrkey)].append(string)
        return list(anagrams.values())