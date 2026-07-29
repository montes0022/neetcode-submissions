class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        smallest = 0
        while left <= right:
            print(f'l:{left} and r:{right}')
            if nums[left] < nums[right]:
                #if the left most is smaller than the right most
                #array is sorted, compare result to leftmost index and break
                smallest = min(smallest, nums[left])
                break

            mid = left + (right - left) // 2

            #l and mid are in the same segment.
            #min element would be in the right part.
            if nums[left] < nums[mid]:
                left = mid + 1.
            #right and mid are in the same segment.
            #minimum element is in the left part.
            elif nums[mid] < nums[right]:
                right = mid - 1


        return smallest