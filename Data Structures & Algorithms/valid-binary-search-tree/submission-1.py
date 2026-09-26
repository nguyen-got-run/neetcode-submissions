from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode], lower: int, upper: int):
        if not node: return
        if not self.ans: return

        val, left, right = node.val, node.left, node.right

        self.ans = lower < val and val < upper

        self.dfs(left, lower, val)
        self.dfs(right, val, upper)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        self.ans = True

        self.dfs(root, -10000, 10000)

        return self.ans