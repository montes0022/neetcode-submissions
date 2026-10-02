class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        output = 0
        numStack = []
        for i in range(len(tokens)):
            if tokens[i] in ops:
                total = 0
                rightOperand = int(numStack.pop())
                leftOperand = int(numStack.pop())

                if tokens[i] == '+':
                    total = leftOperand + rightOperand
                elif tokens[i] == '-':
                    total = leftOperand - rightOperand
                elif tokens[i] == '*':
                    total = leftOperand * rightOperand
                else:
                    total = int(leftOperand / rightOperand)

                numStack.append(total)
            else:
                numStack.append(tokens[i])

        return numStack[0]



            



        