class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        productFromLeft = [1] * n
        productFromRight = [1] * n
        # [01, 02,  08, 48]
        # [48, 48, 24,  06]

        # [48, 24, 12,  8]
        for i in range(n):
            prev = 1 if i-1 < 0 else productFromLeft[i-1]
            num = nums[i]
            productFromLeft[i] = prev * num
        
        for i in range(n-1, -1, -1):
            prev = 1 if i+1 > n - 1 else productFromRight[i+1]
            num = nums[i]
            productFromRight[i] = prev * num
        
        ans = []

        for i in range(n):

            lProd = 1 if i-1 < 0 else productFromLeft[i-1]
            rProd = 1 if i+1 > n - 1 else productFromRight[i+1]

            ans.append(lProd * rProd)
        
        return ans
