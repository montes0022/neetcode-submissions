# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        #save one node right before grouping
        group_prev = dummy_node
        #1 -> 2 -> 3 ->
        #1 -> 3 -> 2 ->
        #group_prev will point to the newly reversed group, like 3-> 2 ->

        while True:
            #start with group_prev since it is not apart of the group
            #return the kth node
            kth = self.getKth(group_prev, k)
            if not kth: #if the kth node does not exist break out of loop.
                break
            #node right after the group
            group_next = kth.next

            #basic reversal
            #prev can be set to None, but issue is we end up with splitting linked list
            #so it should be kth.next, node after kth element.
            prev = kth.next
            #first node in our group we want to reverse
            current = group_prev.next

            #reversal, while current has not reached the end of the group
            while current != group_next:
                after = current.next
                current.next = prev
                prev = current
                current = temp

            #tmp will be used for updating group_prev
            #stores first node in group, again kth is last
            tmp = group_prev.next
            #we want kth (last node in group) to be start of the group
            #one node before start of our group, group_prev
            group_prev.next = kth #this puts kth at start
            group_prev = tmp #with kth now first, group_prev should be last in group

        return dummy.next





    
    def getKth(self, current, k):
        while current and k > 0:
            current = current.next
            kth -=1
        return current

        