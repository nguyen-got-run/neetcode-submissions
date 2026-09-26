class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
    
        def getKey(word: str) -> str:
            ar = [0] * 26
            for ch in word:
                i = ord(ch) - ord('a')
                ar[i] += 1
            return str(ar)
        
        ans = {}
        for word in strs:
            key = getKey(word)
            if key not in ans: ans[key] = []
            ans[key].append(word)
        
        return list(ans.values())
        
        
