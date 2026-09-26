class Solution:
    def is_window_valid(self, ch: str, seen: Set[str]) -> bool:
        return ch not in seen

    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        seen = set()

        for r in range(len(s)):
            ch = s[r]

            while not self.is_window_valid(ch, seen):
                seen.remove(s[l])
                l += 1

            max_len = max(max_len, r - l + 1)
            seen.add(ch)

        return max_len