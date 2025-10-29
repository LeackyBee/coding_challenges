from typing import Optional

from Utils.tree import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        frontier = [root]

        depth = 1
        while frontier:
            nfrontier = []
            for node in frontier:
                # if we have a leaf node, and its sum is the target, return true
                if not (node.left or node.right):
                    return depth
                if node.left:
                    nfrontier.append(node.left)
                if node.right:
                    nfrontier.append(node.right)
            frontier = nfrontier
            depth += 1

