class Solution:
    def isValid(self, s: str) -> bool:
        pdict = { "}" : "{", ")" : "(", "]":"["}
        stack = []

        for char in s:
            #if we are looking at close parenthesis
            #we want to make sure stack is not empty.
            #want to make sure value at the top of the stack
            #is the matching opening parenthesis
            if c in pdict:
                #stack[-1] is the last item in the list
                #so if the last item in the list (top of stack)
                #matches the value of the key which is a closing parenthesis,
                #pop form the stack
                if stack and stack[-1] == pdict[c]:
                    stack.pop()
                else: #parenthesis do not match
                    return False
            else: #if we are looking at an open parenthesis, just add it
                stack.append(c)



        if len(stack) == 0:
            return True
        
        return False

            
        