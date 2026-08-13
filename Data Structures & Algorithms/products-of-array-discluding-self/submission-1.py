class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #at least i got this initialization right
        output = [1] * len(nums)

        #prefix loop.
        pre = 1

        for i in range(len(nums)-1):
            output[i] = pre
            
            #update prefix so that prefix is the product of itself ->
            #and the current element i in nums
            pre *= nums[i]

        #postfix loop
        post = 1

        #for i in range(len(nums)-1, 0, -1): you did this
        #the middle arg is non inclusive, so you would have stopped at second to last.
        for i in range(len(nums)-1, -1, -1):
            #multiply post fix with the value that is already in result.
            output[i] *= post

            post *= nums[i]

        return output

        