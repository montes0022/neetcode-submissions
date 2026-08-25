class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) -1
        area = 0

        while start <= end:
            #logic for calculating area
            height1 = heights[start]
            height2 = heights[end]

            width = end - start

            min_height = min(height1, height2)

            current_area = min_height * width

            #i believe something like this will be needed.
            area = max(area, current_area)

            #when do you shift the start and end pointers?
            if start < len(heights)-1 and heights[start+1] > heights[end-1]:
                start +=1
            else:
                end -= 1

        return area
        