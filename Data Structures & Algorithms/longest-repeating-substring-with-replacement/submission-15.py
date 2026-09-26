class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans, l = 0, 0
        counts = [0] * 26

        for r in range(n):
            idx = ord(s[r]) - ord('A')
            counts[idx] += 1

            # while things are invalid, move l:
            while (r-l+1) - max(counts) > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l +=1
            
            ans = max(ans, r - l + 1)
            r+=1
            
        
        return ans

