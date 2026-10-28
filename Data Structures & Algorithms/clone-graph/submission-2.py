"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        seen = {}
    
        def dfs(node: Node) -> Node:
            # created, return right away
            if node in seen: return seen[node]

            # create a clone
            val, neighbors = node.val, node.neighbors
            clone = Node(val)

            seen[node] = clone

            for each in neighbors:
                clone.neighbors.append(dfs(each))
            
            # created clone, return
            return clone
        
        dfs(node)

        return seen[node]