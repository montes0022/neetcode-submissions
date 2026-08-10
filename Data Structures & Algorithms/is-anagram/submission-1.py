class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for item in s:
            if item not in t:
                return False

        for item in t:
            if item not in s:
                return False

        return True