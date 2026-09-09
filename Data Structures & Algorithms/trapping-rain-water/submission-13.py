class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        LMAX = height[start]
        RMAX = height[end]

        water = 0

        while start < end:

            if LMAX < RMAX:
                start += 1 
                water += max(0, LMAX - height[start])
                LMAX = max(LMAX, height[start])
            else:
                end -= 1
                water += max(0, RMAX - height[end])
                RMAX = max(RMAX, height[end])

        return water

        