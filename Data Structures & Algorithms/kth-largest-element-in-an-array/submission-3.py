import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums: h.append(-num)
        heapq.heapify(h)

        count, prev = 1, heapq.heappop(h)

        while count < k:
            cur = heapq.heappop(h)

            count += 1
            prev = cur
        
        return -prev

