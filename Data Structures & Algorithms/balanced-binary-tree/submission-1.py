# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return 0
        
        left, right = self.dfs(node.left), self.dfs(node.right)

        # update res
        if self.res:
            self.res = abs(left - right) <= 1 

        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        self.dfs(root)

        return self.res
