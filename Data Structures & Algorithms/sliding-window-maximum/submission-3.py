class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        lst = []

        l = 0

        for r in range(k, len(nums)+1):
            winmax = None
            for i in range(l, r):
                winmax = max(nums[i], winmax)
            lst.append(winmax)
            l += 1
        
        return lst