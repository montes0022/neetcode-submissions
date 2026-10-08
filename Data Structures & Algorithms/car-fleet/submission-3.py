class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = []

        #create a list that stores position and spped like (p,s)
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        #sort the list by p
        pairs_sorted = sorted(pairs)

        #in reverse order, loop through the sorted list
        for i in range(len(pairs_sorted)-1, -1, -1):

            #insert your pair at the top of the stack
            stack.append((pairs_sorted[i][0], pairs_sorted[i][1]))

            #when our stack has more than one item, compare the top of the stack
            #with its adjacent item.
            if stack and len(stack) > 1:
                #time of position i is target minus the speed value of pairs_sorted
                #divided by the pos. value at speed_sorted.
                newest = stack.pop()
                adjacent = stack.pop()

                t_newest = (target - newest[0]) / newest[1]
                t_adjacent = (target - adjacent[0]) / adjacent[1]

                #if the top's time to reach target is faster than it's adjacent
                #item, then the car represented by the top of the stack
                #will be bound and now go the same speed as the car ahead of it.
                if t_newest <= t_adjacent:
                    stack.append((adjacent[0], adjacent[1]))
                else:
                    #if not, then that means the top's time to reach target
                    #is slower than it's adjacent item, so therefore the cars
                    #will remain in separate fleets. The top of the stack
                    #will now be the upper bound or the fastest that all cars 
                    #behind will be able to go.
                    stack.append((adjacent[0], adjacent[1]))
                    stack.append((newest[0], newest[1]))

        return len(stack)


        