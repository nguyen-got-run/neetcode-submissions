class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, rows, cols = 0, len(grid), len(grid[0])
        # dirs(x, y) to go: top, right, btm, left
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        seen = set()

        def bfs(r: int, c: int) -> int:
            loc = (r, c)
            q = collections.deque()
            cur = 0
            
            # init
            seen.add(loc)
            q.append(loc)
            cur += 1

            while q:
                qr, qc = q.popleft()

                for dx, dy in dirs:
                    nr, nc = qr + dy, qc + dx
                    nloc = (nr, nc)

                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        nloc not in seen and
                        grid[nr][nc] == 1
                    ):
                        # update
                        seen.add(nloc)
                        q.append(nloc)
                        cur += 1
            return cur

        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]

                if cell == 0 or (r, c) in seen: continue
                size = bfs(r, c)
                ans = max(ans, size)
        
        return ans
        