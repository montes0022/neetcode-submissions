class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        start = 0
        end = len(height) -1
        leftmax = height[start]
        rightmax = height[end]
        
        while start < end:
            #smaller max value gets shifted inward.
            #the formula is MIN(LEFTMAX, RIGHTMAX)
            #whatever condition you go to in here is the min!
            if leftmax < rightmax:
                #move left over first
                start += 1
                #calculate water before updating leftmax
                water += max(0, leftmax - height[start])
                leftmax = max(leftmax, height[start])
            else:
                end -= 1
                water += max(0, rightmax - height[end])
                rightmax = max(rightmax, height[end])
        return water

        