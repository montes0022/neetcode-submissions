# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

       
        #init a current pointer
        current = root
        #swap the position of the children nodes
        current.left, current.right = current.right, current.left
        #recursively call invertTree on both child nodes
        #so that way, we flip their child nodes and so on.
        self.invertTree(current.left)
        self.invertTree(current.right)

        

        return current
        