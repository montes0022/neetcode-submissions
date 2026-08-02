class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            
            if target == nums[mid]:
                return mid

            #left segment -> pivt point is in the right
            if nums[left] <= nums[mid]:
                #if target is bigger than nums[mid] or smaller than nums[l]
                #basically if the target does not lie within the left sorted segment.
                #this condition means target has been rotated to right segment.
                if target > nums[mid] or target < nums[left]:
                    #since target has been rotated out, move left closer to right segment.
                    left = mid + 1
                else:
                    #target is likely already in the left segment, so move right to be within bounds.
                    right = mid - 1
            else: #left is not smaller than mid, so look at the right sorted segment.
                #if target is smaller than nums[mid] or bigger than nums[r]
                #if the target does not lie within the right sorted segment.
                if target < nums[mid] or target > nums[right]:
                    #move right closer to the left sement.
                    right = mid -1
                else:
                    #target is already in the right segment.
                    left = mid + 1

        return -1


        