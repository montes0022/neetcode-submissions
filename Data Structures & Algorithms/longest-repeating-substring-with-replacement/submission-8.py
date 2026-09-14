class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] in chars:
                s[r] += 1
            else:
                s[r] = 1

            freq = max(chars.values())
            current = r - l + 1
            replacements = current - freq

            if replacements > k:
                chars[s[l]] -=1
                l+=1
                current -=1
            output = max(output, current)
        return output







        