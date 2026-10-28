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

        #get longest of the left path
     
        leftsum = self.diameterOfBinaryTree(left)

        #get the longest of the right path
      
        rightsum = self.diameterOfBinaryTree(right)
        #what if both paths are equal? Then I just need to add them both

        if leftsum == 0 and rightsum == 0:
            return 1
        else:
            return 1+max(rightsum, leftsum)


        
