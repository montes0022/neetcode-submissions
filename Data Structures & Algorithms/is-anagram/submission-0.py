class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        for item in s:
            if item not in t:
                return False

        for item in t:
            if item not in s:
                return False

        return True