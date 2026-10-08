class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []



        for i in range(len(heights)):

            while stack and stack[-1][0] < (heights[i] * i+1):
                stack.pop()
                #any other logic
            

            stack.append((heights[i] * i+1, i))
        

        return stack[0][0]