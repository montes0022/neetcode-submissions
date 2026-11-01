# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def traverse(p, q):

            if p is None and q:
                return False
            elif q is None and p:
                return False
            elif p and q and p.val != q.val:
                return False
            else:
                right = traverse(p.left,q.left)
                left = traverse(p.right, q.right)

                if right is False:
                    return False
                if left is False:
                    return False
                else:
                    return True

        return traverse(p,q) is not False
            
        