class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []



        for i in range(len(heights)):

            while stack and stack[-1][0] < (heights[i]):
                stack.pop()
                #any other logic
            

            stack.append((heights[i], i))
        

        return stack[0][0]