class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        nrows, ncols = len(heights), len(heights[0])
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)] #t->r->b->l

        # init for pacific
        pq = collections.deque()
        pseen = set()

        # init for atlantic
        aq = collections.deque()
        aseen = set()


        # first & bottom row
        for i in range(ncols):
            toploc = (0, i)
            btmloc = (nrows-1, i)

            pq.append(toploc)
            pseen.add(toploc)

            aq.append(btmloc)
            aseen.add(btmloc)
        
        # left & right cols
        for i in range(nrows):
            leftloc = (i, 0)
            rightloc = (i, ncols-1)

            pq.append(leftloc)
            pseen.add(leftloc)

            aq.append(rightloc)
            aseen.add(rightloc)

        def bfs(q, s):
            res = set()

            while q:
                for i in range(len(q)):
                    qr, qc = q.popleft()
                    qloc = (qr, qc)
                    res.add(qloc)

                    for dx, dy in dirs:
                        nr, nc = qr + dx, qc + dy
                        nloc = nr, nc

                        if ((nr in range(nrows)) and
                            (nc in range(ncols)) and
                            (nloc not in s) and
                            (heights[nr][nc] >= heights[qr][qc])
                        ):
                            q.append(nloc)
                            s.add(nloc)

            return res
        
        pacifics = bfs(pq, pseen)
        atlantics = bfs(aq, aseen)

        intersects = pacifics.intersection(atlantics)
        ans = []

        for r, c in intersects:
            ans.append([r, c])

        return ans 
        