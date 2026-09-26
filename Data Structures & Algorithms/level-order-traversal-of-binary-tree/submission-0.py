# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, node: Optional[TreeNode], level: int) -> List[int]:
        if not node: return []

        while len(self.res) - 1 < level:
            self.res.append([])
        
        self.res[level].append(node.val)
        
        level += 1
        left, right = node.left, node.right

        self.bfs(left, level)
        self.bfs(right, level)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        self.res = []

        self.bfs(root, 0)

        return self.res



        