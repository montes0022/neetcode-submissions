# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                #return a pointer to the kth node from the end
        #pass in 2, return a pointer that points to the 2nd to last node

        dummy = ListNode()

        dummy.next = head
        prev = dummy

        fast = head
        slow = head

        #check to make sure we do not pass something that is out of bounds. fast will Leap ahead k nodes of slow
        for _ in range(n):
            if(fast is None):
                return None
            fast = fast.next

        #so we know k is in bounds of the ll, while fast is not none, advance fast and slow until the end of the list
        #slow moves at the same speed of fast
        #so because fast had a head start, it will reach the end first, and when that happens, slow will be at the destined spot.

        if fast is None:
            return head.next
        
        while(fast):
            prev = prev.next
            slow = slow.next
            fast = fast.next

        prev.next = slow.next
        slow.next = None

        return head