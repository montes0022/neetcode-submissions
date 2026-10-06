class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:


                item = stack.pop()

                #do something with this pattern.
                output[item[1]] = i - item[1]
            stack.append((temperatures[i], i))

        
        return output

        
                



        