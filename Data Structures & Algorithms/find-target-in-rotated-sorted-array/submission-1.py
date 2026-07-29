class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        smallest = nums[0]

        while left <= right:
            #compute mid
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            #target is probably in the right segment
            if nums[mid] > target:
                left = mid + 1
            #target must be in the left segment
            elif nums[mid] < target:
                right = mid - 1


        return -1
        