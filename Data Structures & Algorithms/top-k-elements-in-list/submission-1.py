class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToCountDict = {}

        for num in nums:
            if num in numToCountDict:
                numToCountDict[num] += 1
            else:
                numToCountDict[num] = 1
        
        countToNumDict = {}
        
        for num in numToCountDict:
            count = numToCountDict[num]
            if count in countToNumDict:
                countToNumDict[count].append(num)
            else:
                countToNumDict[count] = [num]

        counts = [key for key in countToNumDict]
        counts.sort(reverse=True)

        ans = []

        for count in counts:
            nums = countToNumDict[count]
            for num in nums:
                ans.append(num)

        return ans[0:k]

        





        