class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1

        area = 0

        while start < end:

            width = end - start
            curr_area = min(height[start], height[end]) * width

            area = max(curr_area, area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        

        return area
        