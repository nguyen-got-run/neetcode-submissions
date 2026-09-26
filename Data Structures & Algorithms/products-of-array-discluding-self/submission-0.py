class Solution:
    def getTotalProduct(self, nums: List[int]) -> int:
        totalProduct = 1
        
        for num in nums:
            if num == 0:
                return 0
            totalProduct *= num

        return totalProduct

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        curProd = 1

        for i in range(len(nums)):
            num = nums[i]

            restProduct = self.getTotalProduct(nums[i+1:len(nums)])
            ans.append(curProd * restProduct)

            curProd *= num

        return ans

        