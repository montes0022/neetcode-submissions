class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif string[i] == ")":
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
            if s[i] == "[":
                stack.append(s[i])
            elif string[i] == "]":
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()

            if s[i] == "{":
                stack.append(s[i])
            elif string[i] == "}":
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()


        if len(stack) == 0:
            return True
        
        return False

            
        