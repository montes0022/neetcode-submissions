class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ops:
                operation = tokens[i]
    
                total = stack.pop()
    
                total = eval(f'{stack.pop()} {operation} {total}')
    
                stack.append(total)
            else:
                stack.append(tokens[i])
    
        return stack[0]

            



        