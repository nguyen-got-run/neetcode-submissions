# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return -1

        count, ans = k, -1
    
        def dfs(node: Optional[TreeNode]):
            nonlocal count, ans
            if not node: return
            # if len(vals) >= k: return
            if count == 0: return

            l, r, v = node.left, node.right, node.val

            dfs(l)
            # if len(vals) < k:
            #     vals.append(v)
            count -= 1
            if count == 0:
                ans = v
            dfs(r)

        dfs(root)
        return ans
        
        