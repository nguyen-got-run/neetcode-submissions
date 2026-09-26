# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0

        arr = []

        def dfs(node: Optional[TreeNode]):
            if not node: return
            # if len(arr) > k: return

            val, left, right = node.val, node.left, node.right

            if left: dfs(left)
            arr.append(val)
            if right: dfs(right)
        
        dfs(root)

        # print(arr)
        return arr[k-1]


