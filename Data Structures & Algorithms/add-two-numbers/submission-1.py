# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                
                
        dummy = ListNode()

        new_node = dummy

        carry = 0
        curr_one = l1
        curr_two = l2

        while True:
            if curr_one and curr_two:
                index_sum = curr_one.val + curr_two.val + carry

                ones = index_sum % 10        # 8
                carry = index_sum // 10      # 1
                new_node.next = ListNode(ones)

                curr_one = curr_one.next
                curr_two = curr_two.next

                new_node = new_node.next
            elif curr_one and curr_two is None:
                index_sum = curr_one.val + 0 + carry

                ones = index_sum % 10        # 8
                carry = index_sum // 10      # 1
                new_node.next = ListNode(ones)

                curr_one = curr_one.next
                new_node = new_node.next
            elif curr_two and curr_one is None:
                index_sum = 0 + curr_two.val + carry

                ones = index_sum % 10        # 8
                carry = index_sum // 10      # 1
                new_node.next = ListNode(ones)
                curr_two = curr_two.next
                new_node = new_node.next
            else:
                if carry == 1:
                    new_node.next = ListNode(carry)
                return dummy.next