class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        for i in range(len(nums)):
            if nums[i] + nums[i+1]:
                return [i, i+1]