class Solution:
    def climbStairs(self, n: int) -> int:
        oneStep, twoStep = 1, 1

        for i in range(n-1):
            result = oneStep + twoStep
            twoStep = oneStep
            oneStep = result
        
        return oneStep
        