class Solution:
    def getLength(self, left: int, right: int) -> int:
        return right-left
    def getHeight(self, lHeight: int, rHeight: int) -> int:
        return min(lHeight, rHeight)
    def getAmt(self, l: int, h: int) -> int:
        return l*h

    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxAmt = 0

        while left < right:
            length = self.getLength(left, right)
            
            lHeight = heights[left]
            rHeight = heights[right]
            height = self.getHeight(lHeight, rHeight)

            amt = self.getAmt(length, height)

            if amt > maxAmt:
                maxAmt = amt
            
            if lHeight >= rHeight:
                right -= 1
            else:
                left += 1
        
        return maxAmt

