class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lst = []
        heap = []

        #begin loop
        for i in range(len(nums)):
            #use library to manipulate the heap list as a heap.
            #use negative syntax because this heap defaults as a min queue.
            #append nums[i] along with the index to the heap (nums[i], i)
            heapq.heappush(heap, (-nums[i], i))

            #if we are at the position where we are about to leave
            #or we are outside of the boundary k-1, the the window,
            #we need to check if our head of heap is also outside
            #the window.
            if i >= k-1:
                #if and while our head is outside the window
                #keep removing the head of the heap until
                #the head is within our window. This is done by using
                #the index that we add along side the value to the heap
                #so when the index is within i-k. the window, it will be the 
                #max value up to this point.
                while(heap[0][1] <= i - k):
                    heapq.heappop(heap)

                #you must add the - sign here because we inserted the value
                #as a negative at the beginning to make the heap behave like
                #a max heap.
                lst.append(-heap[0][0])

        return lst


