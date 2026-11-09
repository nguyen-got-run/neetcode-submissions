import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]

        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            x, y = heapq.heappop(neg_stones), heapq.heappop(neg_stones)

            if x == y: continue
            else:
                z = -abs(x-y)
                heapq.heappush(neg_stones, z)
        
        return 0 if not neg_stones else -heapq.heappop(neg_stones)
