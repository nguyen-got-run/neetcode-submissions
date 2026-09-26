# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: TreeNode, branchMax: int):
        if not node: return
        val, left, right = node.val, node.left, node.right
        newBranchMax = max(branchMax, val)

        if branchMax <= val:
            self.ans += 1
        
        self.dfs(left, newBranchMax)
        self.dfs(right, newBranchMax)

    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0

        self.dfs(root, root.val)

        return self.ans




        