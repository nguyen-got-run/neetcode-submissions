class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, total = [], n * 2
        if not n: return ans

        def dfs(remain: int, diff: int, cur: str):
            if len(cur) == total:
                ans.append(cur)
                return
            
            # choose to open
            if remain > 0: dfs(remain - 1, diff + 1, cur + '(')

            # choose to close
            if diff > 0: dfs(remain, diff - 1, cur + ')')
    
        dfs(n, 0, '')
        return ans
        