class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        lst = []

        l = 0
        lst.append(max(nums[l:k]))
        for r in range(k, len(nums)+1):
            lst.append(max(nums[l:r]))
            l += 1
        
        return lst