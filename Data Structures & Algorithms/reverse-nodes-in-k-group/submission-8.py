# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = temp = head
        stored_head = None
        counter = 1
        while temp:
            if counter % k == 0:
                next = temp.next
                #sever the kth node from rest of list temporarily
                temp.next = None
                #create a pointer to what would be the node after kth node
                #after_temp = temp.next

                #return the head of the severed, now reversed linked list
                current_reversal = self.reverse_linked_list(start)

                if counter == k:
                    stored_head = current_reversal

                new_temp = current_reversal

                while new_temp.next:
                    new_temp = new_temp.next
                
                new_temp.next = next
                start = next
                
            temp = temp.next
            counter+=1
        
        return stored_head



    
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

        