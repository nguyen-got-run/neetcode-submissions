# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        ans = 0
        def dfs(r: Optional[TreeNode]) -> int:
            nonlocal ans

            if not r: return 0
            countL = dfs(r.left)
            countR = dfs(r.right)
            d = countL + countR
            ans = max(ans, d)
            return 1 + max(countL, countR)
        
        dfs(root)
        return ans


        