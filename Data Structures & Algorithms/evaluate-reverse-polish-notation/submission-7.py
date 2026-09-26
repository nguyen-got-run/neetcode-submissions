class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # def div(a: int, b: int) -> int:
        #     if b == 0: return 0
        #     return math.floor(a/b)
    
        operands = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: 0 if b == 0 else int(a/b)
        }
        st = []
        for token in tokens:
            if token not in operands:
                st.append(int(token))
            else:
                b, a = st.pop(), st.pop()
    
                fnc = operands[token]
                res = fnc(a, b)
                st.append(res)
        
        return st[0]


        