class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict = {}

        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] = True
            else:
                my_dict[nums[i]] = False
        
        for key in my_dict:
            if my_dict[key] is True:
                return key
        