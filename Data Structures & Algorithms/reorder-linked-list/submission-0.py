# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head
        slow = head

        while(fast is not None and fast.next):
            slow = slow.next
            fast = fast.next.next

        #get second half of list
        other_half = slow.next
        slow.next = None


        temp = other_half
        before = None

        #while loops is appropriate - reverse pointers one by one.
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        #point other_half to the new end after reverse
        other_half = before

        l1 = head
        l2 = other_half
        while l1 and l2:
            afterl1 = l1.next
            afterl2 = l2.next

            l1.next = l2
            l2.next = afterl1

            l1 = afterl1
            l2 = afterl2
            
            


        
        