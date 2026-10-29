# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
         #init a member variable so that is is accessable outside of scope (ie, the dfs method below)
        self.res = 0

        #return height
        def getHeight(node):
            if node is None:
                return 0

            #recursively call dfs on left and right nodes
            leftpath = dfs(curr.left)
            rightpath = dfs(curr.right)

            #update the global
            self.res = max(self.res, leftpath+rightpath)

            #return the height of the current node back to the parent/
            return 1 + max(leftpath, rightpath)

        getHeight(root)
        return self.res


        
