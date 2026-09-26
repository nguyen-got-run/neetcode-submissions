class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []

        # m-1 because we're gonna add last row with 1s later
        for row in range(m-1):
            grid.append([0] * n)
        
        # init values on the last col and last row
        # reason is because we can only move right or down
        for row in grid:
            row[-1] = 1
        
        grid.append([1] * n)
    
        for i in range(m-2, -1, -1):
            row = grid[i]
            below_row = grid[i+1]
            for j in range(n-2, -1, -1):
                right_cell = row[j+1]
                below_cell = below_row[j]

                grid[i][j] = right_cell + below_cell

        return grid[0][0]