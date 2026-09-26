class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res, cur = [], []

        def backtracking(i, total):
            if total == target:
                res.append(cur[:])
                return

            if i >= n: return
            if total > target: return

            candidate = candidates[i]
            toAdd = 1

            # choose to add
            cur.append(candidate)
            backtracking(i + toAdd, total + candidate)
            cur.pop()

            # choose not to add
            while i + toAdd < n and candidates[i + toAdd] == candidate:
                toAdd += 1

            backtracking(i + toAdd, total)


        backtracking(0, 0)

        return res
        