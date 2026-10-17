class Solution:
    def countSubstrings(self, s: str) -> int:
        ans, n = 0, len(s)
        if not n: return ans
        if n == 1: return 1

        for i in range(n):
            # odd case
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        
        return ans
        
        