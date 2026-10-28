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

        #the root you pass in with each child, if they have any, 
        #has a length of 1 to each.

        #get the longest of the left path
        leftsum = 0
        leftsum += self.diameterOfBinaryTree(left)


        #get the longest of the right path
        rightsum = 0
        rightsum += self.diameterOfBinaryTree(right)

        #now I need the bigger of the 2 paths
        toreturn = 0
        toreturn = max(leftsum, rightsum)

        return toreturn

