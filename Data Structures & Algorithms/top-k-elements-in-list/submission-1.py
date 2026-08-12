class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = []
        my_dict = {}

        for item in nums:
            my_dict[item] = 1 + my_dict.get(item, 0)

        print(my_dict)

        return None