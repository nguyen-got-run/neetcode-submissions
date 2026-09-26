class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
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


        