class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        lptr = 0 
        rptr = 0 
        lettersToFind = {}

        def isValid(freq):
            for v in freq.values():
                if v > 0:
                    return False 
            return True 

        for c in t:
            lettersToFind[c] = lettersToFind.get(c, 0) + 1

        range = None
        while rptr < len(s):
            if lettersToFind.get(s[rptr]) is not None:
                lettersToFind[s[rptr]] -= 1 

            while isValid(lettersToFind):
                if range == None or range[1] - range[0] > rptr - lptr:
                    range = (lptr, rptr)
                if s[lptr] in t:
                    lettersToFind[s[lptr]] = lettersToFind.get(s[lptr], 0) + 1
                lptr += 1
            
            rptr += 1

        if range == None:
            return "" 
        else:
            return s[range[0]:range[1]+1]