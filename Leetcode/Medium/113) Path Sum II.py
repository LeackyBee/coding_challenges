from typing import Optional, List

from Utils.tree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        frontier = [([root.val], root)]

        output = []

        while frontier:
            nfrontier = []
            for path, node in frontier:
                # if we have a leaf node, and its sum is the target, return true
                if not (node.left or node.right) and sum(path) == targetSum:
                    output.append(path)
                if node.left:
                    nfrontier.append((path + [node.left.val], node.left))
                if node.right:
                    nfrontier.append((path + [node.right.val], node.right))

            frontier = nfrontier

        return output
