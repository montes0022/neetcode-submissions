class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ops:
                operation = tokens[i]
    
                total = 0
                a = int(stack.pop())
                b = int(stack.pop())

                if operation == "/":
                    total = int(a // b)   # truncates toward zero
                else:
                    total = eval(f"{a} {operation} {b}")
    
                stack.append(total)
            else:
                stack.append(tokens[i])
    
        return int(stack[0])

            



        