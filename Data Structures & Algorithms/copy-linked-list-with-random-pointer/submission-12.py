"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {None : None}          # original_node -> copied_node
        curr = head

        while curr:
            # deep copy the node's value
            copied = Node(curr.val)
            # store mapping
            mapping[curr] = copied
            # move forward
            curr = curr.next
        
        temp = head

        while temp:
            node = mapping[temp]
            node.next = mapping[temp.next]
            node.random = mapping[temp.random]
            temp = temp.next

        return mapping[head]
        