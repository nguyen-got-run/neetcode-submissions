class Solution:
    def getSubLen(self, l: int, r: int) -> int:
        return r-l+1
    def isValid(self, l: int, r: int, counts: list[int], k: int) -> bool:
        sub_len = self.getSubLen(l, r)
        return sub_len - max(counts) <= k and l <= r

    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        counts = [0] * 26

        for r in range(len(s)):
            ch = s[r]
            window_len = r - l + 1

            counts[ord(ch) - 65] += 1

            while not self.isValid(l, r, counts, k):
                counts[ord(s[l]) - 65] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)

        return max_len


            
        