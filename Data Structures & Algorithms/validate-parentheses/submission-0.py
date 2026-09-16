class Solution:
    def isValid(self, s: str) -> bool:

        stack = set()

        for par in s:
            
            if par == "}":
                stack.remove("{")

            elif par == "]":
                stack.remove("[")

            elif par == ")":
                stack.remove("(")

            else:
                stack.add(par)

        if len(stack) == 0:
            return True
        
        return False

            
        