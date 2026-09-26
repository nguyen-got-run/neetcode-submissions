class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = max(piles)
        l, r = 1, maxSpeed

        def calcTime(s: int) -> int:
            t = 0
            for p in piles:
                if s >= p:
                    t += 1
                else:
                    t += math.ceil(p/s)
            return t

        ans = maxSpeed + 1
        while l <= r:
            m = (r - l) // 2 + l
            t = calcTime(m)

            if t > h: # eating too slow, need to move l
                l = m + 1
            else: # eating time is good, need to move r to find ans
                ans = min(ans, m)
                r = m - 1
        
        return ans


        