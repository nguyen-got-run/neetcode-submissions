class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        ans = [0] * n
        s = []

        for i in range(n):
            temp = temps[i]
            if not s: s.append((temp, i))
            else:
                while s and s[-1][0] < temp:
                    _, j = s.pop()
                    ans[j] = i - j
                
                s.append((temp, i))
        
        return ans



        