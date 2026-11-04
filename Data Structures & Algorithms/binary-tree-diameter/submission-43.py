# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def traverseAndComputeHeights(root):
            if root is None:
                return 0

            left = traverseAndComputeHeights(root.left)

            right = traverseAndComputeHeights(root.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        traverseAndComputeHeights(root)

        return self.diameter