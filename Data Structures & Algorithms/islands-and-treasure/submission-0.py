class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nrows = len(grid)
        ncols = len(grid[0])
        # dirs to go: t->r->b->l
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        gates = []
        for r in range(nrows):
            for c in range(ncols):
                cell = grid[r][c]
                if cell == 0:
                    gates.append((r, c))
        

        def bfs(r, c):
            visited = set()

            q = collections.deque()
            q.append((r, c, 0))

            while q:
                qr, qc, qdis = q.popleft()

                for dx, dy in dirs:
                    nr, nc = qr + dx, qc + dy
                    npos = (nr, nc)

                    if ((nr in range(nrows)) and
                        (nc in range(ncols)) and
                        (grid[nr][nc] != -1) and
                        (grid[nr][nc] != 0) and
                        (npos not in visited)
                    ):
                        visited.add(npos)
                        dis = qdis + 1
                        
                        nval = grid[nr][nc]
                        # q.append(npos)
                        # grid[nr][nc] = min(nval, dis)
                        if dis < nval:
                            q.append((nr, nc, dis))
                            grid[nr][nc] = min(nval, dis)
                            
        
        for r, c in gates:
            bfs(r, c)
        
