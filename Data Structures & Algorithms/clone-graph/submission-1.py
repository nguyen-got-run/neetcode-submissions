
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        oldToNew = {}

        def dfs(n):
            # already cloned
            if n in oldToNew: return oldToNew[n]

            # create clone
            val, neighbors = n.val, n.neighbors
            clone = Node(val)
            oldToNew[n] = clone

            for neighbor in neighbors:
                # neighbor is an original node
                # so we need to find its cloned version to add to the clone
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        dfs(node)

        return oldToNew[node]
