class Solution:
    def add(self, num1: int, num2: int) -> int:
        return num1 + num2
    
    def sub(self, num1: int, num2: int) -> int:
        return num1 - num2

    def multp(self, num1: int, num2: int) -> int:
        return num1 * num2
    
    def dvd(self, num1: int, num2: int) -> int:
        return int(float(num1) / num2)

    def evalRPN(self, tokens: List[str]) -> int:
        operandToFunc = {'+': self.add, '-': self.sub, '*': self.multp, '/': self.dvd}

        numStack = []

        for each in tokens:
            print(numStack)
            if each not in operandToFunc:
                numStack.append(int(each))
            else:
                num2 = numStack.pop()
                num1 = numStack.pop()

                func = operandToFunc[each]
                ans = func(num1, num2)
                numStack.append(ans)
            
        return numStack.pop()