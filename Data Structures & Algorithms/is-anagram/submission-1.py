class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
    
        ar = [0] * 26
        padding = 97

        for i in range(len(s)):
            charS = s[i]
            charT = t[i]

            ar[ord(charS) - padding] += 1
            ar[ord(charT) - padding] -= 1
        
        for count in ar:
            if count != 0: return False
        
        return True
