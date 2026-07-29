class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right - left) // 2

            #left sorted segment, means min be in right sorted.
            if nums[mid] > nums[left]:
                left = mid + 1
            #if mid and r in sorted segment, min will be in left sorted.
            #means the list is sorted?
            elif nums[mid] < nums[right]:
                right = mid -1


        return nums[mid]