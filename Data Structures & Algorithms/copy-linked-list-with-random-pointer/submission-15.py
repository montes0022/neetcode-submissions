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
            copy = Node(curr.val)
            mapping[curr] = copy
            curr = curr.next

        #start over at head
        temp = head

        while temp:
            mapping[temp].next = temp.next
            mapping[temp].random = temp.random
            temp = temp.next 
        
        return mapping[head]


        