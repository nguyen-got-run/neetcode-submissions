import heapq

class Solution:
    def sqDist(self, p1: List[int], p2: List[int]):
        x1, y1 = p1
        x2, y2 = p2
        return (x1 - x2)**2 + (y1 - y2)**2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        origin = [0, 0]

        for point in points:
            d = self.sqDist(point, origin)
            dis.append([d, point])
        
        heapq.heapify(dis)

        ans = []

        while len(ans) < k:
            d, point = heapq.heappop(dis)
            ans.append(point)

        return ans