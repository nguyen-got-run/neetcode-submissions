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
                # e.g, set(1, 2, 3) -> set(2, 3)
                remain.remove(num)

                subset.append(num)
                dfs()
                subset.pop()

                # after dfs for num, we have to put it back
                # e.g, after processing 1, set(2, 3) -> set(1, 2, 3) 
                remain.add(num)

        dfs()
        return ans
        