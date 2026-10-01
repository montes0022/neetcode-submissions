class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
    
        for i in range(len(temperatures)-1, -1, -1):
            stack.append((temperatures[i], i))
    
        for t in range(len(temperatures)):
            curr = t
    
            while curr< len(temperatures) and temperatures[curr] <= stack[-1][0]:
                curr += 1
    
            popped = stack.pop()
    
            if curr >= len(temperatures):
                res[popped[1]] = t - popped[1]
            else:
                res[popped[1]] = curr - popped[1]
    
    
        return res
                



        