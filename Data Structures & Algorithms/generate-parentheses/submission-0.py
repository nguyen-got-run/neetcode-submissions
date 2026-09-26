class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, cur = [], []

        def backtrack():
            def isValid(curStr: List[str]) -> bool:
                stk = []

                for ch in curStr:
                    if ch == "(": stk.append("(")
                    elif ch == ")":
                        if not stk: return False
                        stk.pop()
                
                return len(stk) == 0

            if len(cur) == 2 * n:
                if isValid(cur[:]):
                    ans.append("".join(cur))
                return
            
            # choose to add open
            cur.append("(")
            backtrack()
            cur.pop()

            # choose to add close
            cur.append(")")
            backtrack()
            cur.pop()

        backtrack()

        return ans