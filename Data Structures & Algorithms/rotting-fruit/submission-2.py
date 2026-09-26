class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        nrows, ncols = len(grid), len(grid[0])
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)] # dirs to go: t->r->b->l
        q = collections.deque()
        fresh_count = 0
        for r in range(nrows):
            for c in range(ncols):
                cell = grid[r][c]
                if cell == 1:
                    fresh_count += 1
                    continue
                if cell == 2:
                    loc = (r, c)
                    q.append(loc)
        
        # if fresh_count == 0: return 0
    
        time = 0
        while q and fresh_count > 0:
            time += 1
            for i in range(len(q)):
                qr, qc = q.popleft()
                for dx, dy in dirs:
                    nr, nc = qr + dx, qc + dy
                    nloc = (nr, nc)
                    if ((nr in range(nrows)) and
                        (nc in range(ncols)) and
                        (grid[nr][nc] == 1)  
                    ):
                        q.append(nloc)
                        fresh_count -= 1
                        grid[nr][nc] = 2
        
        return time if fresh_count == 0 else -1



        