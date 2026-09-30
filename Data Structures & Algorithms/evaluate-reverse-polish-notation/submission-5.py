class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ops:
                operation = tokens[i]
    
                total = stack.pop()
    
                total = int(eval(f'{stack.pop()} {operation} {total}'))
    
                stack.append(total)
            else:
                stack.append(tokens[i])
    
        return int(stack[0])

            



        