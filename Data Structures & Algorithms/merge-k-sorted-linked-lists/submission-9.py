# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy_master = ListNode(0)
        current_master = dummy_master
        index = 0

        while index < len(lists)-1:
            current_master.next = self.merge_two_lists(lists[index], lists[index+1])
            index += 1

        return current_master.next


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

        return dummy.next

        