class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rws, cls = len(grid), len(grid[0])
        ans = 0
        visited = set()
        # dirs(x, y) to go: top, right, btm, left
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        # explore the current island
        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))

            while q:
                qr, qc = q.popleft()
                for dx, dy in dirs:
                    nr, nc, = qr + dx, qc + dy
                    nloc = (nr, nc)

                    if ((nr in range(rws)) and
                        (nc in range (cls)) and
                        grid[nr][nc] == "1" and
                        nloc not in visited
                    ):

                        q.append(nloc)
                        visited.add(nloc)

        for r in range(rws):
            for c in range(cls):
                if grid[r][c] == "0":
                    continue
                
                if (r, c) in visited:
                    continue
                
                # "1"
                ans += 1
                bfs(r, c)

        return ans


        