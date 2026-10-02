class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        output = 0

        numStack = []

        for i in range(len(tokens)):

            if tokens[i] in ops:
                #math

                total = 0
                rightOperand = int(stack.pop())
                leftOperand = int(stack.pop())

                if tokens[i] == "+":
                    total = leftOperand + rightOperand
                if tokens[i] == "-":
                    total = leftOperand - rightOperand
                if tokens[i] == "*":
                    total = leftOperand * rightOperand
                else:
                    total = int(leftOperand / rightOperand)

                numStack.append(total)
            else:
                numStack.append(tokens[i])







        return output



            



        