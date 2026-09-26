from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        ans = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            n = len(queue)

            for i in range(n):
                item = queue.popleft()

                val, left, right = item.val, item.left, item.right
                level.append(val)

                if left: queue.append(left)
                if right: queue.append(right)

            ans.append(level[-1])
        

        return ans

        