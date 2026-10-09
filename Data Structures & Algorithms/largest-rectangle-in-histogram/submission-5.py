class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []


        min_height = (float('inf'),0)

        for i in range(len(heights)):

            if heights[i] < min_height[0]:
                min_height = (heights[i], i)

            area_one = heights[i]
            area_two = (i + 1) * min_height
            area_three = 0


            if i > 0 and heights[i-1] > min_height and heights[i] > min_height:
                area_three = ((i - min_height[1]) + 1) * min(heights[i-1], heights[i])

            heightwant = max(area_one, area_two, area_three)
            while stack and stack[-1] < heightwant:
                stack.pop()
                #any other logic
            
            
            stack.append(heightwant)
        

        return stack[0]