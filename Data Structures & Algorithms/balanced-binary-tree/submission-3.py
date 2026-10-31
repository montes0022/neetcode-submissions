# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.lengthRight = 0
        self.lengthLeft = 0

        def computeHeight(node):
            if node is None:
                return 0

            
            leftpath = computeHeight(node.left)
            rightpath = computeHeight(node.right)

            self.lengthLeft = max(self.lengthLeft, leftpath)
            self.lengthRight = max(self.lengthRight, rightpath)

            return 1 + max(leftpath, rightpath)

        computeHeight(root)
        if self.lengthRight > self.lengthLeft + 1:
            return False
        if self.lengthLeft > self.lengthRight +1:
            return False

        return True
        