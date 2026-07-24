# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        temp = head
        before = None
        counter = 1

        while temp:
            if counter % k == 0:
                after = temp.next
                before = self.reverse_linked_list(temp)
                before.next = after
                start = after
            temp = temp.next
            counter += 1

        return before
            



    
    def reverse_linked_list(self, node):

        temp = node
        before = None

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        #before is where the last pointer ended up.
        return before

        