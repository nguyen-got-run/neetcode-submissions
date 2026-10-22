class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, cache = len(s), {}

        def solve(i: int) -> bool:
            if i >= n: return True
            if i in cache: return cache[i]
            for word in wordDict:
                l = len(word) + i
                cur = s[i:l] 
                ok = cur == word and solve(l)
                cache[i] = ok
                if ok: return True
        
            return False
        
        return solve(0)

