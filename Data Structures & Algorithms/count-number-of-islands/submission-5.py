class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans, rows, cols = 0, len(grid), len(grid[0])
        dirs = [
            # dx, dy
            (0, -1), # top
            (1, 0), # right
            (0, 1), # btm
            (-1, 0) # left
        ]
    
        seen = set()

        def bfs(row: int, col: int):
            seen.add((row, col))
            q = collections.deque()
            q.append((row, col))
            while q:
                r, c = q.popleft()
                
                for dx, dy in dirs:
                    qr, qc = r + dy, c + dx
                    loc = (qr, qc)

                    if (
                        qr in range(0, rows) and
                        qc in range(0, cols) and
                        loc not in seen and
                        grid[qr][qc] == "1"
                    ):
                        seen.add(loc)
                        q.append(loc)
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) in seen: continue
                if grid[row][col] == "0": continue
                ans += 1
                bfs(row, col)
        
        return ans