class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True 
        isAllNonAlpha = True
        for c in s:
            if c.isalnum():
                isAllNonAlpha = False
        if isAllNonAlpha:
            return True
        ptr1 = 0
        ptr2 = len(s)-1
        while ptr1 <= ptr2:
            while not s[ptr1].isalnum():
                ptr1 += 1
            while not s[ptr2].isalnum():
                ptr2 -= 1
            if ptr1 == ptr2:
                return True
            elif s[ptr1].lower() == s[ptr2].lower():
                ptr1 += 1
                ptr2 -= 1
            else:
                return False
        return True 
    