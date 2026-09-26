class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[-1] = True

        newDict = []
        for word in wordDict:
            if len(word) > n: continue
            newDict.append(word)
        
        newDict.sort(key=lambda x: len(x))
        # print(newDict)

        for i in range(n - 1, -1, -1):
            for word in newDict:
                wordLen = len(word)
                newI = i + wordLen
                if(newI <= n and s[i:newI] == word):
                    dp[i] = dp[newI]
                
                if dp[i]:
                    break
            # print('\n')
        return dp[0]

        

