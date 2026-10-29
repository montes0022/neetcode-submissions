# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
globald = 0
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        item = helper(root)

        return globald
        

    def helper(self, root):
        if root is None:
            return 0

        current = root
        right = current.right
        left = current.left
        

        #get longest of the left path
        leftsum = self.helper(left)

        #get the longest of the right path
        rightsum = self.helper(right)
        #what if both paths are equal? Then I just need to add them both

        #it seems that this is returning the height
        #i need the height of both subtrees
        #and I need the best diameter of each subtree
        global globald
        globald = max(globald, leftsum + rightsum)
        return 1 + max(rightsum, leftsum)


        
