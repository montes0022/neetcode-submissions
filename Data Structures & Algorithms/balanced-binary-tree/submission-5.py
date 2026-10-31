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

            left = computeHeight(node.left)
            if left is False:
                return False

            right = computeHeight(node.right)
            if right is False:
                return False

            if abs(left - right) > 1:
                return False

            return 1 + max(left, right)

        return computeHeight(root) is not False

        
        