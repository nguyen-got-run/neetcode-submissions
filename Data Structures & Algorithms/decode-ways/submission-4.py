class Solution:

    def numDecodings(self, s: str) -> int:
        if not s: return 0
        if not int(s[0]): return 0

        def isValid(prevCh: int, curCh: int) -> int:
            if not prevCh: return False
            num = prevCh * 10 + curCh
            return num <= 26
        
        # base case: start at 0th index
        p, c = 1, 1
    
        for i in range(1, len(s)):
            num = int(s[i])
            prev = int(s[i-1])
            cur = 0

            # case 1: can take bth 1-digit and 2-digit
            if num != 0 and isValid(prev, num):
                cur += p
                cur += c
            
            # case 2: can take 1-digit only:
            if num != 0 and not isValid(prev, num):
                cur += c

            # case 3: can take 2-digit only:
            if num == 0 and isValid(prev, num):
                cur += p
            
            # case 4: cannt take bth:
            if num == 0 and not isValid(prev, num):
                return 0
            
            p = c
            c = cur

        return c
