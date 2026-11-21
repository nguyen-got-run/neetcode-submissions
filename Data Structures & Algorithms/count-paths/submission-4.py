class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # relationship: choices[m][n] = choice[m+1][n] + choice[m][n+1] (down and right)
        grid = []

        # m-1 because we're gonna add last row with 1s later
        for row in range(m-1):
            grid.append([0] * n)
        
        # init values on the last col and last row
        # reason is because we can only move right or down
        for row in grid:
            row[-1] = 1
        grid.append([1] * n)
        
        # skip last row and last col
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                grid[row][col] = grid[row+1][col] + grid[row][col+1]
        
        return grid[0][0]