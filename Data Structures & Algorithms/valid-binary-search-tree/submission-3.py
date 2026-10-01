# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(n: Optional[TreeNode], smallest: float, biggest: float) -> bool:
            nonlocal ans
            if not ans: return False
            if not n: return True

            l, r, v = n.left, n.right, n.val
            if not (smallest < v < biggest):
                ans = False
                return False
            
            # left is upper bounded by v, while right is lower bounded by v
            return dfs(l, smallest, v) and dfs(r, v, biggest)
        
        dfs(root, float('-inf'), float('inf'))

        return ans

        