class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            if i in my_dict:
                return [my_dict[i], i]
            else:
                my_dict[target-nums[i]] = i

