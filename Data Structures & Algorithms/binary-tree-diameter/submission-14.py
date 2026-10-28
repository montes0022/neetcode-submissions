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

        leftsum = 0
        leftsum += self.diameterOfBinaryTree(left)

        #get the longest of the right path
        rightsum = 0
        rightsum += self.diameterOfBinaryTree(right)

        #now I need the bigger of the 2 paths
        toreturn = 0
        toreturn = max(leftsum, rightsum)

        return 1+toreturn-1

