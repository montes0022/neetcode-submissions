class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        output = 0

        stack = []

        for i, h in enumerate(heights):
            static = i

            while stack and h < stack[-1][1]:
                index, height = stack.pop()

                output = max(output, (i - index) * h)

                static = index

            stack.append((heights[i], static))


        for i, h in stack:
            output = max(output, (len(heights) - i) * h)


        return output