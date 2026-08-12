class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        #need an extra index to hold the frequency of n where n is len(nums)
        buckets = [[] for i in range(len(nums) + 1)]    
        #hashmap of each number and its frequency in nums
        for item in nums:
            my_dict[item] = 1 + my_dict.get(item, 0)    
        #v is the frequency of k in nums
        for k, v in my_dict.items():
            buckets[v].append(k)    
        res = []
        for i in range(len(buckets)-1, 0, -1):
            #item is the number that appears i times in nums
            #automatically add the collection at buckets[i]
            #since we start at the top, the most frequent items.
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res

