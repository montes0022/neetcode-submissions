# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = temp = head
        stored_head = None
        before = None
        counter = 1
        while temp:
            if counter % k == 0:
                print('============================')
                print(f'counter: {counter}')
                print(f'value of start is : {start.val}')
                print(f'value of temp is : {temp.val}')
                next = temp.next
                #sever the kth node from rest of list temporarily
                temp.next = None
                #create a pointer to what would be the node after kth node
                #after_temp = temp.next

                #return the head of the severed, now reversed linked list
                current_reversal = self.reverse_linked_list(start)
                print(f'value of current_reversal is : {current_reversal.val}')

                new_temp = current_reversal

                while new_temp.next:
                    new_temp = new_temp.next

                if counter == k:
                    print(f'counter: {counter} equals {k}! stored head for answer')
                    stored_head = current_reversal

                if before:
                    before.next = current_reversal
                before = temp
                temp = new_temp
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

        