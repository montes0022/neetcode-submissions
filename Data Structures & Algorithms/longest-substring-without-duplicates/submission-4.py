class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        window = 0

        for r in range(len(s)):
            #the point of this while loop is for chars to be clear to 'reset the streak'
        #also so that we move l to 'catch up to r' so that way current_window gets set to 1.
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            #r-l+1 is the current window where r is always the right boundary and l will catch up and equal r
        #as soon as we find that s[r] exists in our set.
            current_window = (r-l + 1)
            window = max(window, current_window)

        return window