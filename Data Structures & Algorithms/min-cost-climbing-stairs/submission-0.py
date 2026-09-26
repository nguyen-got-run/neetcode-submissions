class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        oneStep, twoStep = cost[n-2], cost[n-1]
        
        for i in range(n-3, -1, -1):
            print(i)
            cur_cost = cost[i]
            new_one = min(cur_cost + oneStep, cur_cost + twoStep)
            twoStep = oneStep
            oneStep = new_one

        return min(oneStep, twoStep)