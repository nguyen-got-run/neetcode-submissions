class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 1, 1
        
        for i in range(1, n):
            temp = prev
            prev = cur
            cur += temp
        
        return cur