class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n, prev, cur = len(cost), 0, 0

        for i in range(2, n+1):
            temp = prev
            prev = cur

            cur = min(temp + cost[i-2], cur + cost[i-1])
        
        return cur