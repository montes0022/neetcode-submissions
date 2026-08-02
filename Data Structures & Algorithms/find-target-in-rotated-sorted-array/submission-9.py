class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            
            if target == nums[mid]:
                return mid

            #left segment
            if nums[left] <= nums[mid]:
                #if target is bigger than nums[mid] or smaller than nums[l]
                if target > nums[mid] or target < nums[l]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: #right segment
                #if target is smaller than nums[mid] or bigger than nums[r]
                if target < nums[mid] or target > nums[r]:
                    right = mid -1
                else:
                    left = mid + 1

        return -1


        