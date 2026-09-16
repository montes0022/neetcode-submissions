class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                stack.append(s[i])
            else:
                if i > 0 and s[i] == "}" and stack[i-1] == "{":
                    if len(my_stack.stack_list) == 0:
                        return False
                    stack.pop(s[i-1])
                if i > 0 and s[i] == ")" and stack[i-1] == "(":
                    if len(my_stack.stack_list) == 0:
                        return False
                    stack.pop(s[i-1])
                if i > 0 and s[i] == "]" and stack[i-1] == "[":
                    if len(my_stack.stack_list) == 0:
                        return False
                    stack.pop(s[i-1])


        if len(stack) == 0:
            return True
        
        return False

            
        