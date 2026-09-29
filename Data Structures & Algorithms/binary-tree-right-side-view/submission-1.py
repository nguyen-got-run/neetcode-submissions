# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return ans

        q = deque([root])

        while q:
            for i in range(len(q)):
                n = q.popleft()
                left, right = n.left, n.right
                if left: q.append(left)
                if right: q.append(right)
            
            # n now is reference to the last node of the previous level:
            ans.append(n.val)
        
        return ans
        