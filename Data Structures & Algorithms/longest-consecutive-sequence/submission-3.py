class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        my_dict = {}

        for num in nums:
            if num-1 not in my_dict:
                count += 1
            my_dict[num] = True

        return count
        