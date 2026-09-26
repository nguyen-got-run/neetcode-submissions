class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temps)
        
        for i in range(len(temps)):
            tmp = temps[i]

            while stack and stack[-1][0] < tmp:
                stk_tmp, stk_i = stack.pop()
                ans[stk_i] = i - stk_i
            stack.append((tmp, i))
                


        return ans        











