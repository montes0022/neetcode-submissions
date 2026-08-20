class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                streak = 1
                while num + 1 in num_set:
                    streak += 1
                count = max(count, streak)
            

        return count
        