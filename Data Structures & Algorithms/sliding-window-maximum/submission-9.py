class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        lst = []

        l = 0

        for r in range(k, len(nums)+1):
            winmax = max(my_list[l:r])
            lst.append(winmax)
            l += 1
        
        return lst