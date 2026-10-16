class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not n: return s
        if n == 1: return s

        ans = 0
        L, R = 0, 1
        for i in range(n):
            # check odd case
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length > ans:
                    ans = length
                    L = l
                    R = r
                
                l -= 1
                r += 1
            
            # check for even case
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length > ans:
                    ans = length
                    L = l
                    R = r
                
                l -= 1
                r += 1
        
        return s[L:R+1]





        