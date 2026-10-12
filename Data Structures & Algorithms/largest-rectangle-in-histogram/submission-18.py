class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        output = 0
        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:
                item = stack.pop()

                left = 0

                if stack:
                    left = stack[-1]

                output = max(((i-1) - left)*heights[item], output)

            stack.append(i)

        return output