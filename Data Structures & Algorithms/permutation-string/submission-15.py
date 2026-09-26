class Solution:
    def getCharIndex(self, ch: str) -> int:
        return ord(ch) - 97

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(s1_len):
            s1_counts[self.getCharIndex(s1[i])] += 1
            s2_counts[self.getCharIndex(s2[i])] += 1

        if s1_counts == s2_counts:
            return True

        for i in range(s1_len, s2_len):
            ch = s2[i]
            ch_to_del = s2[i - s1_len]

            s2_counts[self.getCharIndex(ch)] += 1
            s2_counts[self.getCharIndex(ch_to_del)] -= 1

            if s1_counts == s2_counts:
                return True

        return False


            