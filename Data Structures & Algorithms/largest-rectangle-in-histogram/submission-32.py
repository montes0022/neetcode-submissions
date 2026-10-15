class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        output = 0

        stack = []

        for i in range(len(heights)):
            static = i

            while stack and heights[i] < stack[-1][0]:
                height, index = stack.pop()

                output = max(output, (i - index) * height)

                static = index

            stack.append(heights[i], static)


        for i, h in stack:
            output = max(output, (len(heights) - i) * h)


        return output