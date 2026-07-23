# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #reverse head and tail
        temp = head
        before = None

        #while loops is appropriate - reverse pointers one by one.
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        head = before
        return head
        