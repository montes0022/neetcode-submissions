# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if the root/node we pass in is None, it is not a subtree of subRoot
        #which is not None
        if root is None and subRoot is not None:
            return False

        #we are checking root against subroot
        #if root is not a subTree of subRoot, see if it's left or right node's
        #children are. This is done recursively. If any node is found in any side
        #of the tree that is a subtree of subRoot, then it would return True and
        #bubble the result up to the first call.
        if not self.isSameTree(root, subRoot):
            return (self.isSubtree(curr.left, subRoot) or self.isSubtree(curr.right, subRoot))

        #if they are found to be the same tree, return True up.
        return True
        
    #borrowed from the solution of isSameTree!
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False

        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))