# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        found_node = self.find_node(root, subRoot.val)

        if found_node:
            return self.isSameTree(found_node, subRoot)
        else:
            return False



    def find_node(self, root, target):
        if not root:
            return None

        if root.val == target:
            return root

        left_result = self.find_node(root.left, target)
        if left_result:
            return left_result

        return self.find_node(root.right, target)

    
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False

        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))