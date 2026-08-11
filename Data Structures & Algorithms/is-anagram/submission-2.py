class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for item in s:
            countS[item] = 1 + countS.get(item, 0)
            countT[item] = 1 + countT.get(item, 0)
        return countS == countT