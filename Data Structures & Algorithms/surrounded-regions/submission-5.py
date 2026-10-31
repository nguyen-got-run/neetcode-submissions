class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        marked = set()

        def bfm(r: int, c: int):
            loc = (r, c)
            q = collections.deque()

            q.append(loc)
            marked.add(loc)

            while q:
                qr, qc = q.popleft()

                for dx, dy in dirs:
                    nr, nc = qr + dy, qc + dx
                    nloc = (nr, nc)

                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        board[nr][nc] == 'O' and
                        nloc not in marked
                    ):
                        marked.add(nloc)
                        q.append(nloc)

        for row in range(rows):
            if board[row][0] == '0':
                bfm(row, 0)
            if board[row][cols - 1] == 'O':
                bfm(row, cols - 1)
        
        for col in range(cols):
            if board[0][col] == 'O':
                bfm(0, col)
            if board[rows - 1][col] == 'O':
                bfm(rows - 1, col)

        for row in range(1, rows-1):
            for col in range(1, cols-1):
                loc = (row, col)
                if loc not in marked:
                    board[row][col] = 'X'        
        
