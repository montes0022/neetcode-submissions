class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        window = 0

        for r in range(len(s)):
            if s[r] in chars:
                chars.remove(s[r])
                l += 1
            chars.add(s[r])
            window = max(window, r-l + 1)

        return window