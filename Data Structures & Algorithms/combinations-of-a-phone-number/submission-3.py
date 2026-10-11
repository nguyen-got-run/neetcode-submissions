class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans, n = [], len(digits)
        if not n: return ans

        digitMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        def dfs(i: int, prev: str):
            if i == n:
                ans.append(prev)
                return
            
            d = digits[i]
            options = digitMap[d]
            for option in options:
                cur = prev + option
                dfs(i + 1, cur)

        
        dfs(0, '')

        return ans