# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        current = root
        right = current.right
        left = current.left

        #pass in a parent
        #if a parent has at least one child, that counts as a level
        #pass in the children that exist
        #so on and so forth
        #had the right idea, just made it more complicated

        #when you pass in a node with no children, each call for the left
        #and right will return 0 thanks to the beginning IF at the top
        #you add at least one to the result to consider the parent itself
        #as a level.
        return 1 + max(self.maxDepth(left), self.maxDepth(right))



        