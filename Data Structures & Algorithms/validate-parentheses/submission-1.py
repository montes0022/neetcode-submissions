class Solution:
    def isValid(self, s: str) -> bool:

        stack = set()

        for par in s:
            
            if par == "}" and "{" in stack:
                stack.remove("{")

            elif par == "]" and "[" in stack:
                stack.remove("[")

            elif par == ")" and "(" in stack:
                stack.remove("(")

            else:
                stack.add(par)

        if len(stack) == 0:
            return True
        
        return False

            
        