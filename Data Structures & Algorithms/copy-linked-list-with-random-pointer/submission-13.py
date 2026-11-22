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

        #create a base dict to store nodes and keys and copies and vals
        mapping = {None:None}
        curr = head
        #basic ll traversal, but create deep copies of nodes only for each og node.
        while curr:
            copy = Node(curr.value)
            mapping[curr] = copy
            curr = curr.next

        #connect the copied nodes based on their corresponding keys.

        for item in mapping:
            mapping[item].next = item.next
            mapping[item].random = item.random

        
        return mapping[head]


        