class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        l, r = 0, n - 1

        def getCurArea():
            w = r - l
            h = min(heights[l], heights[r])
            return w * h

        while l < r:
            curArea = getCurArea()
            ans = max(ans, curArea)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return ans

        