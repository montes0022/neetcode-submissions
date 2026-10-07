class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        pairs = []
    
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
    
        pairs_sorted = sorted(pairs)
    
        for i in range(len(pairs_sorted)-1, -1, -1):
        
            #insert the speed to the top of the stack
            stack.append((pairs_sorted[i][0], pairs_sorted[i][1]))
    
            if stack and len(stack) > 1:
                #time of position i is target minus the speed value of pairs_sorted
                #divided by the pos. value at speed_sorted.
                newest = stack.pop()
                adjacent = stack.pop()
    
                t_newest = (target - newest[0]) / newest[1]
                t_adjacent = (target - adjacent[0]) / adjacent[1]
    
                if t_newest < t_adjacent:
                    stack.append((adjacent[0], adjacent[1]))
                else:
                    stack.append((adjacent[0], adjacent[1]))
                    stack.append((newest[0], newest[1]))
    
    
        return len(stack)

        