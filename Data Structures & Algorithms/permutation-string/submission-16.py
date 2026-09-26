class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1: return False

        cts1 = [0] * 26
        for ch in s1:
            cts1[ord(ch) - ord('a')] += 1
        
        l, r = 0, n1 - 1
        
        while r < n2:
            cts2 = [0] * 26
            for i in range(l, r +1):
                ch = s2[i]
                if cts1[ord(ch) - ord('a')] == 0: # wrong immidiately
                    l += 1
                    r += 1
                    break
                
                cts2[ord(ch) - ord('a')] += 1

                if cts2[ord(ch) - ord('a')] > cts1[ord(ch) - ord('a')]:
                    l += 1
                    r += 1
                    break
            
            if cts1 == cts2:
                return True
            
        
        return False
