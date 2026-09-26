class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        count = 0

        for i in range(n):
            # check palin odd case (cac)
            l, r = i, i
            while (
                (l >= 0) and
                (r < n) and
                s[l] == s[r]
            ):
                count += 1
                l -= 1
                r += 1

            # check palin even case
            l, r = i, i + 1
            while (
                (l >= 0) and
                (r < n) and
                s[l] == s[r]
            ):
                count += 1
                l -= 1
                r += 1
        
        
        return count