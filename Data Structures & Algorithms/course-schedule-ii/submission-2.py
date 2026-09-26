class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            adjMap[c].append(p)

        
        visited = set()
        inAns = set()
        ans = []

        def dfs(c):
            if c in inAns: return True
            if c in visited: return False
            adjLi = adjMap[c]

            # if not adjLi:
            #     ans.append(c)
            #     inAns.add(c)
            #     return True
            
            visited.add(c)

            for each in adjLi:
                if each in inAns: continue
                if not dfs(each): return False
            
            visited.remove(c)
            # adjLi[c] = []
            ans.append(c)
            inAns.add(c)
            return True

        
        for c in range(numCourses):
            if not dfs(c): return []
    
        return ans