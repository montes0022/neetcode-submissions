class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #pairs
        output = 0

        for i, h in enumerate(heights):

            store = i

            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                #area = height you popped * width measured by currentpostion - 
                #popped position.
                output = max(output, height * (i-index))

                store = index
            stack.append((store,h))

        for item, value in stack:

            output = max(output, value * (len(heights) - item))





        return output