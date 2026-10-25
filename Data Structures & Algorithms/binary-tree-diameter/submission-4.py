# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        current = root
        right = current.right
        left = current.left

        #pass in a parent
        #if a parent has at least one child, that counts as a level
        #pass in the children that exist
        #so on and so forth
        return max(self.diameterOfBinaryTree(left), self.diameterOfBinaryTree(right)) -1