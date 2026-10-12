class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        output = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < heights[stack[-1][1]]:
                index, height = stack.pop()

                output = max(output, height * (i - index))

                start = index

            stack.append((start, h))

        for item, height in stack:
            output = max(output, height * (len(heights) - item))

        return output