class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # dirs(x, y) to go: top, right, btm, left
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        
        def bfs(q, s):
            while q:
                for i in range(len(q)):
                    qr, qc = q.popleft()

                    for dx, dy in dirs:
                        nr, nc = qr + dy, qc + dx
                        nloc = (nr, nc)
                        if (
                            nr in range(rows) and
                            nc in range(cols) and
                            nloc not in s and
                            (
                                heights[qr][qc] <= heights[nr][nc] if qr in range(rows) and qc in range(cols) else True
                            )
                        ):
                            q.append(nloc)
                            s.add(nloc)

        # pacific starting points and sets
        q1, s1 = collections.deque(), set()
        for col in range(cols):
            loc = (-1, col)
            q1.append(loc)
            s1.add(loc)
        
        for row in range(rows):
            loc = (row, -1)
            q1.append(loc)
            s1.add(loc)
        
        bfs(q1, s1)

        # atlantic starting points and sets
        q2, s2 = collections.deque(), set()
        for col in range(cols):
            loc = (rows, col)
            q2.append(loc)
            s2.add(loc)
        
        for row in range(rows):
            loc = (row, cols)
            q2.append(loc)
            s2.add(loc)
        
        bfs(q2, s2)

        ans = []
        for row in range(rows):
            for col in range(cols):
                loc = (row, col)
                if (loc in s1) and (loc in s2):
                    ans.append([row, col])
        
        return ans