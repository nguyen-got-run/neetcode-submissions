class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        target = total // 2

        seen = set()
        seen.add(0)

        for num in nums:
            news = []
            for each in seen:
                new = each + num
                if new == target: return True
                news.append(new)
            seen.update(news)
        return False
        