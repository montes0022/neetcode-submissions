# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        #create double ended queue
        queue_p = deque([p])
        queue_q = deque([q])
        #while queue is populated
        while queue_p:
            #pop the start of the queue
            node = queue_p.popleft()
            if node and node.left:
                #append the left child node to the queue
                queue_p.append(node.left)
            else:
                queque_q.append(None)
            if node and node.right:
                #append the right child node to the queue
                queue_p.append(node.right)
            else:
                queque_q.append(None)

        while queue_q:
            #pop the start of the queue
            node = queue_q.popleft()
            if node and node.left:
                #append the left child node to the queue
                queue_q.append(node.left)
            else:
                queque_q.append(None)
            if node and  node.right:
                #append the right child node to the queue
                queue_q.append(node.right)
            else:
                queque_q.append(None)

        if queue_p == queue_q:
            return True
        else:
            return False
            
        