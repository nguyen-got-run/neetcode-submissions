class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return 0

        n = len(s)
        longest = 0
        l, r = 0, 0

        def getSubstringLen(l: int, r: int) -> int:
            return r - l + 1

        for i in range(n):
            # expand l-r for odd case (like cac):
            l1, r1 = i, i

            while ((l1 >= 0) and
                (r1 < n) and
                s[l1] == s[r1]
            ):
                subLen = getSubstringLen(l1, r1)
                if subLen >= longest:
                    longest = subLen
                    l = l1
                    r = r1
                l1 -= 1
                r1 += 1
            
            # expand l-r for even case (like caac)
            l1, r1 = i, i + 1
            while ((l1 >= 0) and
                (r1 < n) and
                s[l1] == s[r1]
            ):
                subLen = getSubstringLen(l1, r1)
                if subLen >= longest:
                    longest = subLen
                    l = l1
                    r = r1
                l1 -= 1
                r1 += 1
        return s[l:r+1]