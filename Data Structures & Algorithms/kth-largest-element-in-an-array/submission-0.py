class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = list(map(lambda n: -n, nums))
        heapq.heapify(neg_nums)

        count = k
        # ans = -1

        while count != 0:
            largest = -heapq.heappop(neg_nums)
            # ans = largest
            count -= 1
        
        return largest
        