class Solution:
    def findOrder(self, numCourses: int, preqs: List[List[int]]) -> List[int]:
        courseRange = range(numCourses)
        adjMap = {i: set() for i in courseRange}

        for c, p in preqs:
            adjMap[c].add(p)

        ans, appended, seen = [], set(), set()
        def dfs(i: int) -> bool:
            # already checked and appended before, so we skip
            if i in appended: return True

            # this check is for the dfs branch
            if i in seen: return False

            adjLi = adjMap[i]
            seen.add(i)
            for p in adjLi:
                if not dfs(p): return False
            
            # because we already have the first check in appended
            # we can even remove these 2 lines
            adjMap[i] = set()
            seen.remove(i)

            # after done exploring, we start to update the ans
            # because of the dfs nature, the preqs will be appended first before the course
            appended.add(i)
            ans.append(i)
            
            return True
        
        for i in courseRange:
            if not dfs(i): return []

        return ans