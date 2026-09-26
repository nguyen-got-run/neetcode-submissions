# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self):
        self.res.append([])
        toMerge = []

        while len(self.q):
            item = self.q.pop(0)
            if item:
                toMerge.append(item)
                self.res[-1].append(item.val)
        
        for each in toMerge:
            self.q.append(each.left)
            self.q.append(each.right)

        if not toMerge:
            self.res.pop(-1)
            return
        
        self.bfs()

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        self.q = []
        self.res = []

        self.q.append(root)
        self.bfs()

        return self.res



        