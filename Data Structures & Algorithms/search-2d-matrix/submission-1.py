class Solution:
    def binSearchIdx(self, nums: List[int], target: int) -> (int, int):
        l = 0
        r = len(nums) - 1
        idx = -1

        while l<=r:
            m = l + (r-l) // 2
            val = nums[m]

            if val == target:
                idx = m
                break

            if val < target:
                l = m + 1
            else:
                r = m - 1
        
        return idx, l

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lasts = [row[-1] for row in matrix]

        found, rowIdxToSearch = self.binSearchIdx(lasts, target)
        if rowIdxToSearch >= len(matrix):
            return False

        if found >= 0:
            return True
        
        idx, _ = self.binSearchIdx(matrix[rowIdxToSearch], target)

        return idx >= 0