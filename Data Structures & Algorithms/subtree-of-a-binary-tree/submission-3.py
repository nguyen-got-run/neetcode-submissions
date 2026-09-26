
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
            # if r: print(r.val)
            # else: print(' not r ')

            # if s: print(s.val)
            # else: print(' not s ')
            # print('\n')
            if not r and not s: return True
            if not r or not s: return False

            if r.val != s.val: return False
            return isSameTree(r.left, s.left) and isSameTree(r.right, s.right)
        
        q = deque([root])

        while q:
            item = q.pop()
            left, right, val = item.left, item.right, item.val

            if val == subRoot.val:
                isLeft = isSameTree(left, subRoot.left)
                isRight = isSameTree(right, subRoot.right) if isLeft else False
                if isLeft and isRight: return True
            
            if left: q.append(left)
            if right: q.append(right)
        
        return False

        