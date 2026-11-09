import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        heapq.heapify(self.h)
        self.n = k

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)

        return heapq.nlargest(self.n, self.h)[-1]

