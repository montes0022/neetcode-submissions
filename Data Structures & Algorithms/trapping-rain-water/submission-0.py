class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        start = 0
        end = len(height) -1
        leftmax = 0
        rightmax = 0
        prefix_height = []
        prefix_max = 0
        for i in range(len(height)):
            if i > 0:
                prefix_max = max(prefix_max, height[i-1])
    
            prefix_height.append(prefix_max)
    
        postfix_height = []
        postfix_max = 0
    
        for i in range(len(height)-1, -1, -1):
                if i < len(height)-1:
                    postfix_max = max(postfix_max, height[i+1])
        
                postfix_height.append(postfix_max)
    
        left_counter = 0
        right_counter = len(postfix_height) -1
    
        for i in range(len(height)):
            left = prefix_height[left_counter]
            right = postfix_height[right_counter]
    
            smallest = min(left, right)
            current_water = smallest - height[1]
    
            current_water = max(0, current_water)
    
            water += current_water
    
            left_counter +=1
            right_counter -=1
    
        return water

        