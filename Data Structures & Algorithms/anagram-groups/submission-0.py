class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        for each in strs:
            arLen = ord('z') - ord('a')
            ar = [0 for _ in range(arLen)]
            for char in each:
                idx = ord(char) - ord('a')
                ar[idx] += 1

            key = str(ar)
            
            if key in myMap:
                curList = myMap[key]
                curList.append(each)
            else:
                myMap[key] = [each]
   
        return list(myMap.values())