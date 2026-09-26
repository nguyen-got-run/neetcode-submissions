class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return

        nrows, ncols = len(board), len(board[0])
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        
        visited = set()
        
        borders = []

        for i in range(nrows):
            left, right = board[i][0], board[i][ncols - 1]

            if left == 'O': borders.append((i, 0))
            if right == 'O': borders.append((i, ncols - 1))
        
        for i in range(ncols):
            top, btm = board[0][i], board[nrows - 1][i]

            if top == 'O': borders.append((0, i))
            if btm == 'O': borders.append((nrows - 1, i))

        def dfs(r, c):
            visited.add((r, c))

            for dx, dy in dirs:
                nx, ny = r + dx, c + dy
                nloc = (nx, ny)

                if ((nx in range(nrows)) and
                    (ny in range(ncols)) and
                    (nloc not in visited) and
                    board[nx][ny] == 'O'
                ):
                    dfs(nx, ny)

        # explore all regions fromm borders
        for r, c in borders:
            dfs(r, c)

        # update everything
        for r in range(nrows):
            for c in range(ncols):
                if (r, c) not in visited:
                    board[r][c] = 'X'
    