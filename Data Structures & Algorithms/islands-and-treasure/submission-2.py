class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        # dirs(x, y) to go: top, right, btm, left
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def bfs(r: int, c: int):
            # print(r, c)
            loc = (r, c)
            q = collections.deque()
            ct = 0

            q.append([loc])

            while q:
                ct += 1

                them = q.popleft()
                # print(str(them))
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
                # print(str(lvls))
                # q.append(lvls)
                if lvls: q.append(lvls)
            # print()

        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                if cell == 0:
                    bfs(r, c)

        
        # return grid

        