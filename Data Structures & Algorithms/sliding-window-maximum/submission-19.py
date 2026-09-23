class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lst = []
        heap = []

        l = 0

        if len(heap) == 0:
            for i in range(k):
                heap.append(nums[i])
                index_of_value = len(heap)-1
                

        for r in range(k, len(nums)):


            l += 1