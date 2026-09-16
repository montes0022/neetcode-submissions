class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        lst = []

        l = 0
        r = k
        while r <= len(nums):
            winmax = max(nums[l:r])
            lst.append(winmax)
            r+=1
            l += 1
        
        return lst