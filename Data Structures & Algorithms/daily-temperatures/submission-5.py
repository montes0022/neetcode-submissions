class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

   

        for t in range(len(temperatures)):
    
            while stack and temperatures[t] > stack[-1][0]:
                popped = stack.pop()
                res[popped[1]] = t - popped[1]

            stack.append((t, temperatures[t]))

        
        return res
                



        