class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2: return len(text1)
        nr, nc = len(text1), len(text2)
        grid = []

        for i in range(nr + 1):
            grid.append([0] * (nc + 1))
        
        #   c a t
        # c 1
        # r   0
        # a
        # b
        # t

        for r in range(nr-1, -1, -1):
            # corresponding char on row
            rch = text1[r]
            # btm row
            br = r + 1
            for c in range(nc-1, -1, -1):
                # corresponding char on col
                cch = text2[c]
                # right col
                rc = c + 1

                if rch == cch:
                    grid[r][c] = 1 + grid[br][rc]
                else:
                    grid[r][c] = max(
                        grid[br][c],
                        grid[r][rc]
                    )

        return grid[0][0]




        