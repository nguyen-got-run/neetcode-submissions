class MedianFinder:
    def __init__(self):
        self.sm = []
        self.lg = []
        # conds for heaps: they have to roughly equal in size (n-vs-n or n-vs-n+1)
        # and all elements on the lg heap >= all elements on the small heap

    def addNum(self, num: int) -> None:
        # add to max heap by default
        heapq.heappush(self.sm, -num)

        # check conds and adjust if needed:
        if (self.sm and self.lg and
            # biggest of sm > smallest of lg
            -self.sm[0] > self.lg[0]):

            # this is the reason why we have to implement
            # maxheap for the sm heap
            el = -heapq.heappop(self.sm)
            heapq.heappush(self.lg, el)
        
        if (len(self.sm) - len(self.lg) > 1):
            el = -heapq.heappop(self.sm)
            heapq.heappush(self.lg, el)
        
        if (len(self.lg) - len(self.sm) > 1):
            el = -heapq.heappop(self.lg)
            heapq.heappush(self.sm, el)
    
    def findMedian(self) -> float:
        sm, lg = self.sm, self.lg

        if not sm and not lg: return None

        if not sm: return lg[0]
        if not lg: return -sm[0]

        if len(sm) == len(lg):
            smallestLg = lg[0]
            biggestSm = -sm[0]
            return (smallestLg + biggestSm) / 2
        
        return lg[0] if len(lg) > len(sm) else -sm[0]


        
        