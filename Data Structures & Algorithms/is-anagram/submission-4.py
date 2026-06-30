class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sFreq = [(chr(i), 0) for i in range(97, 123)]
        tFreq = [(chr(i), 0) for i in range(97, 123)]
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            num1 = ord(char1) - 97
            num2 = ord(char2) - 97
            sFreq[num1] = (char1, sFreq[num1][1]+1)
            tFreq[num2] = (char2, tFreq[num2][1]+1)

        for i in range(len(sFreq)):
            print(sFreq[i], ", ")
            print(tFreq[i], "\n")
            if (sFreq[i][1] != tFreq[i][1]):
                return False
        return True
            

