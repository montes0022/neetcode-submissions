class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        mid = (left + right) // 2

        while True:
            if nums[mid] < target:
                right = mid
            elif nums[mid] > target:
                left = mid

            if nums[mid] is target:
                return mid

        return -1