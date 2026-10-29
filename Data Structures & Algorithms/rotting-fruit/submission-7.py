class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # dirs(x, y) to go: top, right, btm, left
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        fresh, seen = 0, set()

        def bfs() -> int:
            nonlocal fresh
            q = collections.deque()
            ct = 0

            for each in seen:
                q.append(each)
            
            while q:
                print(str(q))
                for i in range(len(q)):
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
                            grid[nr][nc] = 2
                            fresh -= 1
                            seen.add(nloc)
                            q.append(nloc)
                ct += 1
            
            return ct -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    seen.add((r, c))

        if not seen and not fresh: return 0
        if not seen and fresh: return -1

        time = bfs()

        if fresh > 0: return -1
        return time


        