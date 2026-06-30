class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            
            arrkey = [0] * 26
            for i in range(26):
                arrkey[i] = string.count(chr(i + ord('a')))
            arrkey = tuple(arrkey)

        
            anagrams[arrkey].append(string)
        return list(anagrams.values())