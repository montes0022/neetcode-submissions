# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def computeHeight(node):
            if node is None:
                return 0

            leftHeight = computeHeight(node.left)
            if leftHeight is False:
                return False

            rightHeight = computeHeight(node.right)
            if rightHeight is False:
                return False

            if abs(leftHeight - rightHeight) > 1:
                return False

            return 1 + max(leftHeight, rightHeight)

        return computeHeight(root) is not False

        

        
        