class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, cur = [], dict()

        def backtrack():
            if len(cur) == n:
                ans.append(list(cur.keys()))
                return
            
            for num in nums:
                if num not in cur:
                    cur[num] = True
                    backtrack()
                    del cur[num]

        backtrack()
        return ans