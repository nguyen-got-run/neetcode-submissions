# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        if not root: return ans
        # ans += 1

        def dfs(node: Optional[TreeNode], maxVal: int):
            nonlocal ans
            if not node: return
            if node.val >= maxVal:
                ans += 1
            
            newMax = max(maxVal, node.val)
            dfs(node.left, newMax)
            dfs(node.right, newMax)

        dfs(root, -1000)

        return ans