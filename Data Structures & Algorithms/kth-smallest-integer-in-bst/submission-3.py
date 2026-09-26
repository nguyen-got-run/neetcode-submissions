# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0

        count = k
        res = root.val

        def dfs(node: Optional[TreeNode]):
            nonlocal count, res

            if not node: return
            # if len(arr) > k: return

            val, left, right = node.val, node.left, node.right

            dfs(left)
            # if count == 0:
            #     return
            count -= 1
            if count == 0:
                res = val
                return

            dfs(right)
        
        dfs(root)

        # print(arr)
        # return arr[k-1]
        return res


