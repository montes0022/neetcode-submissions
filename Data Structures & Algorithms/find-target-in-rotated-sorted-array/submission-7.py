class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            print(f'l:{left} and r:{right}')
            if nums[left] < nums[right]:
                #if the left most is smaller than the right most
                #array is sorted, compare result to leftmost index and break
                break

                
            
            #compute mid
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            #l and mid are in the same segment.
            #min element would be in the right part.
            if nums[left] <= nums[mid]:
                left = mid + 1
            #right and mid are in the same segment.
            #minimum element is in the left part.
            else:
                right = mid - 1


        return -1
        