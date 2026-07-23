class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 #initialize fast and slow at head
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break #when slow and fast equal, first intersection has been found

        #intialize slow pointer 2, when slow pointer 2 and slow pointer are equal
        #they will represent the start of the loop
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break

        return slow