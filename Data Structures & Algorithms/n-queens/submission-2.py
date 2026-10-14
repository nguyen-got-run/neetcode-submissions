class Solution:
    def solveNQueens(self, n: int) -> List[tuple[int, int]]:
        ans = []
        if not n: return ans

        def isSafe(queens: List[tuple[int, int]], r, c) -> bool:
            for qr, qc in queens:
                # check horizontal and vertical
                if qr == r or qc == c: return False
                # check diagonally
                if abs(qr - r) == abs(qc - c): return False
            return True
        
        def genBoard() -> List[tuple[int, int]]:
            boards = []
            for i in range(len(ans)):
                queens = set(ans[i])

                board = []
                for r in range(n):
                    row = ['.' for _ in range(n)]
                    for c in range(n):
                        if (r, c) in queens:
                            row[c] = 'Q'
                    
                    board.append(''.join(row))
                boards.append(board)
            return boards
    
        subset = []
        def dfs(r: int):
            # base case: when r == n, we have the answer!
            if r == n:
                ans.append(subset[:])
                return
            
            # for each row level, try each column to see if we can add to our current subset
            for c in range(n):
                # if a position (r, c) is safe (cannot be attacked by other queens on prev rows)
                if isSafe(subset, r, c):
                    subset.append((r, c)) # add that pos to our subset
                    dfs(r + 1) # explore the next row and do the same job
                    subset.pop() # done with this row, pop out our subset
            
        dfs(0)
        return genBoard()