class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        start = 0
        end = len(height) -1

        #initialize the left and right max boundaries.
        leftmax = height[start]
        rightmax = height[end]
        
        while start < end:
            #smaller max value gets shifted inward.
            #the first part of the formula is MIN(LEFTMAX, RIGHTMAX)
            #whatever condition you go to in here represents the min!

            #think about it, here, it does not matter what rightmax is,
            #it can be 100000, 50, or 3, leftmax will always be smaller, therefore,
            #MIN(LEFTMAX, RIGHTMAX) is LEFTMAX
            #the opposite for this is in the else condition

            #when we are in each of these conditions we use either leftmax
            #or rightmax in the first part of the equation to find water
            if leftmax < rightmax:
                #move left over first
                start += 1
                #calculate water before updating leftmax
                water += max(0, leftmax - height[start])
                #check for the bigger between leftmax and height[start]
                #update leftmax with the bigger number
                leftmax = max(leftmax, height[start])
            else:
                #move right over first
                end -= 1
                #calculate water before updating rightmax
                water += max(0, rightmax - height[end])
                #check for the bigger between rightmax and height[end]
                #update rightmax with the bigger number
                rightmax = max(rightmax, height[end])
        return water

        