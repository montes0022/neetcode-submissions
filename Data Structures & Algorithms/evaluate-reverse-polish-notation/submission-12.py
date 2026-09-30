class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}

        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] in ops:
                operation = tokens[i]
    
                a = int(stack.pop())
                b = int(total)
                
                if operation == '+':
                    total = a + b
                elif operation == '-':
                    total = a - b
                elif operation == '*':
                    total = a * b
                else:  # division
                    total = int(a / b)  
                    
                stack.append(total)
            else:
                stack.append(tokens[i])
    
        return int(stack[0])

            



        