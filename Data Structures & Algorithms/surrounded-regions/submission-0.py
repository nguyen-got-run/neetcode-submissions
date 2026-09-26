class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return

        nrows, ncols = len(board), len(board[0])
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        
        visited = set()
        regions = []
        cannots = []

        def bfs(r, c):
            loc = (r, c)
            q = collections.deque()
            region = []
            can = False

            visited.add(loc)
            q.append(loc)

            while q:
                qr, qc = q.popleft()
                qloc = (qr, qc)
                region.append(qloc)

                for dx, dy in dirs:
                    nr, nc = qr + dx, qc + dy
                    nloc = nr, nc

                    if (nr not in range(nrows) or nc not in range(ncols)):
                        can = True

                    if ((nr in range(nrows)) and
                        (nc in range(ncols)) and
                        (nloc not in visited) and
                        (board[nr][nc] != 'X')
                    ):
                        visited.add(nloc)
                        q.append(nloc)

            regions.append(region)
            cannots.append(can)

        for r in range(nrows):
            for c in range(ncols):
                cell = board[r][c]
                loc = (r, c)

                if cell == 'X': continue
                if loc in visited: continue

                print(loc)
                bfs(r, c)
        
        for i in range(len(regions)):
            cannot = cannots[i]

            if cannot: continue

            region = regions[i]

            for r, c in region:
                board[r][c] = 'X'