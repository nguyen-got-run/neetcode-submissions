class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not len(grid): return 0

        rws, cls = len(grid), len(grid[0])
        ans = 0
        visited = set()
        # x, y of top-right-btm-left
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def bfs(r, c):
            loc = (r, c)
            visited.add(loc)

            q = collections.deque()
            q.append(loc)

            size = 1

            while q:
                qr, qc = q.popleft()
                for dx, dy in dirs:
                    nr, nc = qr + dx, qc + dy
                    nloc = (nr, nc)

                    if ((nr in range(rws)) and
                        (nc in range(cls)) and
                        (grid[nr][nc] == 1) and
                        (nloc not in visited)
                    ):
                        visited.add(nloc)
                        q.append(nloc)
                        size += 1
            
            return size
        
        for r in range(rws):
            for c in range(cls):
                if grid[r][c] == 0:
                    continue
                
                if (r, c) in visited:
                    continue
                
                island_size = bfs(r, c)
                ans = max(ans, island_size)
        
        return ans
        