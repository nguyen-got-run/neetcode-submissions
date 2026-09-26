class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2: return False
        total = sum(nums)
        if total % 2 == 1: return False
        target = total // 2
        
        dp = set()
        dp.add(0)

        for num in nums:
            next_dp = set()
            for each in dp:
                # 2 options: include num or not
                # not including
                next_dp.add(each)

                # including
                new_sum = each + num
                if new_sum == target: return True
                if new_sum > target: continue
                next_dp.add(new_sum)
            dp = next_dp
        return False

