class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        cts = []

        for num in nums:
            cts.append([])
            if num not in freq: freq[num] = 0
            freq[num] += 1

        for key in freq:
            ct = freq[key]
            # if not cts[ct]: cts[ct] = []
            cts[ct-1].append(key)
        
        ans = []
        for i in range(len(cts) - 1, -1, -1):
            els = cts[i]
            if len(ans) < k:
                for el in els:
                    ans.append(el)
            else:
                return ans
    
        return ans
        