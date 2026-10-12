class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        output = 0

        for i in range(len(heights)):
            start = i
            while stack and heights[i] < heights[stack[-1]]:
                item = stack.pop()

                output = max(output, heights[i] * (i - item))

                start = item

            stack.append(start)

        for item in stack:
            output = max(output, heights[item] * (len(heights) - item))

        return output