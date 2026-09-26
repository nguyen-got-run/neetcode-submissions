from collections import deque
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

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            res.append(level)

        return res


        