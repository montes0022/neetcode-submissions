class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        mid = (left + right) // 2

        while left <= right:
            if nums[mid] < target:
                left = mid
                mid = (left + right) // 2
            elif nums[mid] > target:
                right = mid
                mid = (left + right) // 2

            if nums[mid] == target:
                return mid

        return -1