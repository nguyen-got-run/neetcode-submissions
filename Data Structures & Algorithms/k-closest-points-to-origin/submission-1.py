class Solution:
    def getDistanceToOrigin(sel, point: List[int]) -> float:
        x1, y1 = point[0], point[1]

        return x1**2 + y1**2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            dist_sq = self.getDistanceToOrigin(point)
            minHeap.append((dist_sq, point))
        
        heapq.heapify(minHeap)
        ans = []

        while len(ans) < k:
            dist, point = heapq.heappop(minHeap)
            ans.append(point)
        
        return ans

        