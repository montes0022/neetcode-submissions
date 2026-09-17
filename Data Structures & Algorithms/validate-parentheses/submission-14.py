class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "}":"{", "]":"["}
        stack = []


        for item in s:
            if item in brackets:
                if stack[-1] == brackets[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
            #if item is not a closing bracket
                #add item to the stack
            #if item is a closing bracket
                #is the top of the stack the corresponding opening bracket
                    #if it is, pop the last item in list/top of stack
                    #if not return false

        if len(stack) == 0:
            return True
        
        return False


            
        