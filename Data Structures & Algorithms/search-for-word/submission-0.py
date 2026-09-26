class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        word_len = len(word)
        seen_paths = set()


        def backtrack(row_i, col_i, word_i):
            if word_i == word_len: return True
            if (row_i < 0 or
                row_i >= num_rows or
                col_i <  0 or
                col_i >= num_cols or
                board[row_i][col_i] != word[word_i] or
                (row_i, col_i) in seen_paths
            ): return False

            seen_paths.add((row_i, col_i))
            next_word_i = word_i+1
            ans = (
                backtrack(row_i - 1, col_i, next_word_i) or
                backtrack(row_i + 1, col_i, next_word_i) or
                backtrack(row_i, col_i - 1, next_word_i) or
                backtrack(row_i, col_i + 1, next_word_i) 
            )
            
            seen_paths.remove((row_i, col_i))

            return ans

        for ri in range(num_rows):
            for ci in range(num_cols):
                ans = backtrack(ri, ci, 0)
                if ans: return True
        
        return False