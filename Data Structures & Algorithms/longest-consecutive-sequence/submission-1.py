class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        my_dict = {}

        for num in nums:
            if num not in my_dict:
                my_dict[num] = True


        for key in my_dict:
            while True:
                if key+1 in my_dict:
                    count +=1
                break

        return 0
        