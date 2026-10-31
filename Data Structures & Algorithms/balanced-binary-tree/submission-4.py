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

            if rightpath is False or leftpath is False:
                return False
            elif leftpath > rightpath + 1:
                return False
            elif rightpath > leftpath + 1:
                return False

            #self.lengthLeft = max(self.LengthLeft, leftpath)
            #self.lengthRight = max(self.lengthRight, rightPath)

            return 1 + max(leftpath, rightpath)

        answer = computeHeight(root)

        if answer is False:
            return False
        else:
            return True

        
        