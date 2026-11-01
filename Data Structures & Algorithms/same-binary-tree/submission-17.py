# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #empty trees, return true
        if q is None and p is None:
            return True 
        #one of the tress is empty
        #you can do 'if q is None OR p is None' here
        if q is None and p:
            return False
        if p is None and q:
            return False    
        #values are not equal.
        #this can be merged to if above.
        #'if not p or not q or p.val != q.val'
        if p and q and p.val != q.val:
            return False
       
        #if both nodes survived bases cases, compare recursively both trees.
        #'and' both calls together
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right))
            
        