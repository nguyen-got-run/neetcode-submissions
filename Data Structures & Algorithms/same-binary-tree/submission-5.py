# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q: return True
        # if not p: return False
        # if not q: return False

        cont = True

        def dfs(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            nonlocal cont

            if not cont: return False

            if not n1 and not n2: return True
            if not n1: return False
            if not n2:
                print('n2 empty - False')
                return False

            if n1.val != n2.val:
                cont = False
                return False
            
            branch = dfs(n1.left, n2.left) and dfs(n1.right, n2.right)
            if not branch: cont = False
            
            return branch
        
        return dfs(p, q)

            


        
        