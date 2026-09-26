class Solution:
    def isPalindrome(self, s: List[str]) -> bool:
        if not s: return False
        leftI = 0
        rightI = len(s) - 1

        while leftI <= rightI:
            leftCh = s[leftI]
            rightCh = s[rightI]

            if not leftCh.isalnum():
                leftI += 1
                continue
            
            if not rightCh.isalnum():
                rightI -= 1
                continue
            
            if leftCh.lower() != rightCh.lower():
                return False
            
            leftI += 1
            rightI -= 1
        
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans, cur = [], []

        def dfs(i):
            if i == n:
                ans.append(cur[:])
                return
            
            for j in range(i, n):
                substr = s[i:j+1]
                if self.isPalindrome(substr):
                    # print(i)
                    # print(j)
                    # print(substr)
                    # print('\n')
                    cur.append(substr)
                    dfs(j+1)
                    cur.pop()

        dfs(0)

        return ans
        