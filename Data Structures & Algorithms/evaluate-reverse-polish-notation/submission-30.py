class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []


        for i in range(len(tokens)):

            if(tokens[i] in operators):
                rightop = int(stack.pop())
                leftop = int(stack.pop())

                result = 0
                if tokens[i] == "+":
                    result = leftop + rightop
                elif tokens[i] == "-":
                    result = leftop - rightop
                elif tokens[i] == "*":
                    result = leftop * rightop
                else:
                    result = int(leftop / rightop)

                stack.append(result)
            else:
                stack.append(tokens[i])

        return int(stack[-1])



        