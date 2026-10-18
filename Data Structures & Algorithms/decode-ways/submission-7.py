class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0": return 0

        def ok1(c: int) -> bool:
            return 1 <= c <= 26

        def ok2(p: int, c: int) -> bool:
            if p == 0: return False
            if p >= 3: return False

            return p * 10 + c <= 26
    
        prev, cur = 1, 1

        for i in range(1, n):
            p, c = int(s[i-1]), int(s[i])
            climb1, climb2 = ok1(c), ok2(p, c)

            if not climb1 and not climb2: return 0
            temp = prev
            prev = cur

            if climb1 and climb2: cur = temp + cur
            elif climb2: cur = temp
            else: cur = cur

        return cur 
