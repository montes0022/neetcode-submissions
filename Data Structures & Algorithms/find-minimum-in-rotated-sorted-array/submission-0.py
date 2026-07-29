class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        #mid = (left + right) // 2

        # Instead of (left + right) // 2
        # Preventing integer overflow
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        return -1