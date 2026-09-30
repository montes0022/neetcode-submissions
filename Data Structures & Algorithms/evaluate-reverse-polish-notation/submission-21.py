class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}

        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] in ops:
                #set a total that will be added to the top of the stack
                total = 0
                #b represents the left part of the operator
                #b is inserted last onto the stack, first out

                #a represetns the right part of the operator
                #a is inserted first onto the stack, last out

                #to perform in order of operations relative to how the 
                #numbers are inserted in the tokens array,
                #b is left of the operator, top of stack
                #a is right of the operator, bottom of stack

                #pop two items from the stack only
                #why? because the reverse polish notation states that
                #operands can only operate on two numbers
                a = int(stack.pop())
                b = int(stack.pop())


                #eval was too slow, although the solution was technically correct
                #instead just id the operators on if conditions
                #
                if tokens[i] == '+':
                    total = b + a
                elif tokens[i] == '-':
                    total = b - a
                elif tokens[i] == '*':
                    total = b * a
                else:  # division
                    total = int(b / a)  

                #total is added to the top of the stack and will be 
                #prioritized the next time we encounter an operator
                stack.append(total)
            else:
                #add your number to the stack
                stack.append(tokens[i])
    
        #the stack will only contain one item at this point.
        #the top, and only item, of the stack will be the final
        #answer of the reverse polish notation thingy.
        return int(stack[0])

            



        