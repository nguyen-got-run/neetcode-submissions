# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        
        def dfs(r: Optional[TreeNode]) -> bool:
            nonlocal ans
            if not ans: return 0
            if not r: return 0

            countL, countR = dfs(r.left), dfs(r.right)
            diff = abs(countL - countR)

            if diff > 1:
                ans = False

            return 1 + max(countL, countR)
        
        dfs(root)

        return ans

        