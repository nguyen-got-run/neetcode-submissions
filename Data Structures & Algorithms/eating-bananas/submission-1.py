import math

class Solution:
    def getTotal(self, piles: List[int], s: int) -> int:
        total = 0
        for pile in piles:
            time = math.ceil(pile/s)
            total += time
        
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = 0
        total = 0
        for pile in piles:
            maxSpeed = max(maxSpeed, pile)
            total += pile

        minSpeed = math.ceil(total / h)

        l = minSpeed
        r = maxSpeed
        res = maxSpeed

        while l <= r:
            m = l + (r-l) // 2

            t = self.getTotal(piles, m)

            if t > h:
                l = m + 1
            else:
                r = m - 1
                res = min(res, m)

        
        return res



