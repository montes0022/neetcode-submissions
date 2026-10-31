# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def observeheight(node):
            if node is None:
                return 0

            leftpath = observeheight(node.left)
            rightpath = observeheight(node.right)

            self.res = max(self.res, leftpath + rightpath)
            

            return 1 + max(leftpath, rightpath)

        observeheight(root)
        return self.res


        
