# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque([root])
        ans = []

        while q:
            vals = []

            for i in range(len(q)):
                node = q.popleft()
                val, left, right = node.val, node.left, node.right

                if left: q.append(left)
                if right: q.append(right)
                vals.append(val)

            ans.append(vals)
        
        return ans

        