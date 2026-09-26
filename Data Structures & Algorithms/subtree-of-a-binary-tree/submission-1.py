# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, x: Optional[TreeNode], y: Optional[TreeNode]) -> bool:
        if not x and not y: return True
        if not x or not y: return False
        if x.val != y.val: return False

        return (
            self.isSameTree(x.left, y.left) and
            self.isSameTree(x.right, y.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        return (
            self.isSameTree(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
       
            


        