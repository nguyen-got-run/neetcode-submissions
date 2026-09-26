class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n_stones = []
        for stone in stones:
            n_stones.append(-stone)
        
        heapq.heapify(n_stones)

        while len(n_stones) > 1:
            max1 = -heapq.heappop(n_stones)
            max2 = -heapq.heappop(n_stones)

            if max1 == max2:
                continue
            
            new_weight = abs(max1 - max2)
            heapq.heappush(n_stones, -new_weight)
        
        if not n_stones:
            return 0
        
        return -n_stones[0]
