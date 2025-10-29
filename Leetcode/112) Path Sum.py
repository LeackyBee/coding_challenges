from typing import Optional

from Utils.tree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        frontier = [(root.val, root)]

        while frontier:
            nfrontier = []
            for path_sum, node in frontier:
                # if we have a leaf node, and its sum is the target, return true
                if not (node.left or node.right) and path_sum == targetSum:
                    return True
                if node.left:
                    nfrontier.append((path_sum + node.left.val, node.left))
                if node.right:
                    nfrontier.append((path_sum + node.right.val, node.right))

            frontier = nfrontier

        return False