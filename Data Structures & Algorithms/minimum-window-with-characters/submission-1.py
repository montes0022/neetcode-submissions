class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        output = ""
        #do we need to keep track of the frequencies of the 
        #characters in t?



        #the output will at least be the length of s
        output = ""
        