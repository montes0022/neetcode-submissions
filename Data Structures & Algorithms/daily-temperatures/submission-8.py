class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        #begin loop with index and temperature variables
        for index, temperature in enumerate(temperatures):
            #while our stack is not empty, and while 
            #the temperature we are looking at is bigger than the top
            #of the stacks temperature...
            while stack and temperature > stack[-1][0]:
                #pop from the stack, store the temperature and index in these two
                #variables
                #stacksTemperature = stack.pop()[0]
                #stacksIndex = stack.pop()[1]
                stacksTemperature, stacksIndex = stack.pop()
                #after we pop, calculate the current index - the stacks index
                #set the difference to res' stackIndex position
                res[stacksIndex] = index - stackIndex

            #anyways, append the (temp, temp's index) to your stack
            #you did this outside the while loop when we should have been
            #adding it in this lone for loop
            stack.append((temperature, index))

        
        return res
                



        