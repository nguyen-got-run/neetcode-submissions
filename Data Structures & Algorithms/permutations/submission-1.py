class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        if not n: return ans

        remain = set(nums)
        subset = []
        def dfs():
            if len(subset) == n:
                ans.append(subset[:])
                return
            
            for num in nums:
                if num not in remain:
                    continue
                
                # num is in remain, choose it and pop from the remain
                remain.remove(num)

                subset.append(num)
                dfs()
                subset.pop()

                remain.add(num)

        dfs()
        return ans
        