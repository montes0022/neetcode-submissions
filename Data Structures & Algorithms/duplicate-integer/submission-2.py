class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}

        for item in nums:
            if item not in store:
                store[item] = True
            else:
                return True

        return False


        