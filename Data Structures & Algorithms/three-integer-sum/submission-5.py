class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3: return []
        nums.sort()
        ans = []
        i = 0
        while i < n - 2:
            num = nums[i]
            if i - 1 >= 0 and num == nums[i - 1]:
                i += 1
                continue

            l = i + 1
            r = n -1

            def goLeftBy(r, i):
                shift = 1
                num = nums[r]
                while r - shift > i and num == nums[r - shift]:
                    shift += 1
                
                return shift
            
            def goRightBy(l):
                shift = 1
                num = nums[l]
                while l + shift < n and num == nums[l + shift]:
                    shift += 1
                
                return shift
            
            while l < r:
                left, right = nums[l], nums[r]
                total = num + left + right

                if total == 0:
                    ans.append([num, left, right])
                    shift = goLeftBy(r, i)
                    r -= shift
                    shift = goRightBy(l)
                    l += shift
                elif total > 0: # too large, need right pointer to go left
                    shift = goLeftBy(r, i)
                    r -= shift
                else: # total < 0, too small, need left pointer to go right
                    shift = goRightBy(l)
                    l += shift

            i += 1
        return ans
            

        