class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def search(row: List[int]) -> int:
            l, r = 0, len(row)

            while l<=r:
                m = (r - l ) // 2 + l
                num = row[m]
                if num == target:
                    return True
                if num < target:
                    l = m + 1
                else: # num > target
                    r = m - 1
            
            return False

        
        for i in range(len(matrix)):
            row = matrix[i]

            if target < row[0] or target > row[-1]:
                continue
            
            if search(row): return True
        
        return False

        