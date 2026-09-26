class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, n = 0, len(s) - 1
        l, r = 0, 0
        seen = set()
        print(r)
        print(n)

        while r <= n:
            nxt = s[r]
            
            # is valid
            if nxt not in seen:
                seen.add(nxt)
                ans = max(ans, r - l + 1)
                r += 1
            else: # not value
                while nxt in seen:
                    seen.remove(s[l])
                    l += 1
        
        return ans