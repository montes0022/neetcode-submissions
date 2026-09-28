class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lst = []
        #create a deque, doubly ended queue.
        queue = deque()
        l = 0
        r = 0

        #traverse r over nums
        while r < len(nums):
            #check if the deque is not empty
            #then check if the rightmost item from the deque
            #is smaller than what we want to add.
            while queue and nums[queue[-1]] < nums[r]:
                #while the rightmost number is smaller than what we want to add
                #we need to keep removing it.
                #we remove it until the deque is empty or until a rightmost number
                #is bigger than what we want to add.
                queue.pop()
            #finally, we can append the number we want to add to the deque.
            queue.append(r)

            #if
            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                lst.append(nums[queue[0]])
                l += 1
            r += 1

        return lst


