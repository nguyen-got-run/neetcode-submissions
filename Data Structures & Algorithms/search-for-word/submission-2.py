class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, n = len(board), len(board[0]), len(word)
        visited = [[False for i in range(cols)] for j in range(rows)]
        def dfs(r: int, c: int, cur: int):
            if cur == n: return True
            if r >= rows or r < 0: return False
            if c >= cols or c < 0: return False
            if visited[r][c]: return False
            ch = board[r][c]
            if ch != word[cur]: return False

            # now ch == word[cur], we start checking
            # mark this cell as visited before checking the next ones
            visited[r][c] = True

            nxt = cur + 1
            ans =(
                dfs(r + 1, c, nxt) or 
                dfs(r - 1, c, nxt) or
                dfs(r, c + 1, nxt) or
                dfs(r, c - 1, nxt))
            
            # done traversing, unmark this call as visited
            visited[r][c] = False
            return ans

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True

        return False
        