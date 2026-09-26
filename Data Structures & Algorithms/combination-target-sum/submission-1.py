class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = nums.sort()
        n = len(nums)

        res, cur = [], []

        def dfs(i, total):
            if (total == target):
                res.append(cur[:])
                return
            if i >= n: return
            if total > target: return
            
            # not to add
            dfs(i+1, total)

            # add
            num = nums[i]
            cur.append(num)
            dfs(i, total + num)
            cur.pop()
        
        dfs(0, 0)
        return res




        