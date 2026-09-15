class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maximum = 0
        l = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            current = r-l+1
            maximum = max(maximum, current)

        return maximum



