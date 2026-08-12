class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need an extra index to hold the frequency of n where n is len(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        my_dict = {}

        #hashmap of each number and its frequency in nums
        for item in nums:
            my_dict[item] = 1 + my_dict.get(item, 0)
        #iterate over keys and values with my_dict.items()
        #num is the key, count is the value
        #each index at bucket represents a count, where buckets[i] is a list that->
        #stores the numbers in nums that appeared i times.
        #1 appears once, 2 appears twice, 3 appears three times, so:
        #buckets[1] will have 1
        #buckets[2] will have 2
        #buckets[3] will have 3
        #if you added two 4's , and one 5 to nums [1,2,2,3,3,3,4,4,5]
        #buckets would look like:
        #buckets[1] will have 1,5
        #buckets[2] will have 2,4
        #buckets[3] will have 3
        #count is the frequency of num in nums
        for num, count in my_dict.items():
            buckets[count].append(num)

        #initialize a res variable that will store the top k items.
        res = []
        #iterate thru buckets, start at the last index-1, go to 0, at a rate of -1
        #(going from last to first.)
        for i in range(len(buckets) - 1, 0, -1):
            #so if you start at 5, this means the numbers in buckets[5] appeared 5 times.
            #you are starting at the biggest frequency here in buckets
            #so these are already the most frequent numbers
            #if this frequency of i in buckets[i] has nothing, we ->
            #won't loop and we will go down to the next biggest frequency
            for num in buckets[i]:
                res.append(num)
                #if our count of res == k, you have your k frequent numbers.
                if len(res) == k:
                    return res

