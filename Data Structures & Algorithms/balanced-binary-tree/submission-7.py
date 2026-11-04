# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def computeHeights(root):
            if root is None:
                return 0

            leftHeight = computeHeights(root.left)
            if leftHeight is False:
                return False

            rightHeight = computeHeights(root.right)
            if rightHeight is False:
                return False

            if abs(left-height) > 1:
                return False


            return 1 + max(leftHeight, rightHeight)


        return computeHeights(root) is not False







        
        