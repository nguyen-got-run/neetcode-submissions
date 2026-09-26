class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nrows = len(grid)
        ncols = len(grid[0])
        # dirs to go: t->r->b->l
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        visited = set()
        q = collections.deque()
        for r in range(nrows):
            for c in range(ncols):
                cell = grid[r][c]
                if cell == 0:
                    loc = (r, c)
                    q.append(loc)
                    visited.add(loc)
        
        dis = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dis

                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    nloc = nr, nc

                    if ((nr in range (nrows)) and
                        (nc in range (ncols)) and
                        (grid[nr][nc] != -1) and
                        (nloc not in visited)
                    ):
                        q.append(nloc)
                        visited.add(nloc)
            
            dis += 1
        



