# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy_master = None
        index = 0

        while index < len(lists)-1:
            dummy_master = self.merge_two_lists(lists[index], dummy_master)
            index += 1

        return dummy_master


    def merge_two_lists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next

        current.next = list1 if list1 else list2


        #og return dummy.next
        return dummy.next

        