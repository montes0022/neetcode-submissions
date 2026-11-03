# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        current = root
        target = subRoot.val
        
        while current:
            if target == current.val:
                return self.isSameTree(current, subRoot)
            elif target < current.val:
                current = current.left
            else:
                current = current.right

        return False
        




    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return None

        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))