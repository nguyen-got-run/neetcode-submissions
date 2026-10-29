class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        # dirs(x, y) to go: top, right, btm, left
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def bfs(locs: List[tuple[int, int]]):
            q = collections.deque()
            ct = 0

            q.append(locs)

            while q:
                ct += 1

                them = q.popleft()
                seen = set()
                lvls = []

                for qr, qc in them:
                    for dx, dy in dirs:
                        nr, nc = qr + dy, qc + dx
                        nloc = (nr, nc)

                        if (
                            nr in range(rows) and
                            nc in range(cols) and
                            nloc not in seen and
                            grid[nr][nc] > 0 and
                            ct < grid[nr][nc]
                        ):
                            grid[nr][nc] = ct
                            seen.add(nloc)
                            lvls.append(nloc)
                if lvls: q.append(lvls)

        treasures = []
        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                if cell == 0:
                    treasures.append((r, c))
        
        bfs(treasures)

        
        # return grid

        