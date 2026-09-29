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
            nodes = []
            vals = []

            while q:
                node = q.popleft()
                val, left, right = node.val, node.left, node.right

                if left: nodes.append(left)
                if right: nodes.append(right)
                vals.append(val)

            ans.append(vals)
            for n in nodes:
                q.append(n)
        
        return ans

        