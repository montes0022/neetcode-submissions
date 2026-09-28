class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        chars = {}
        output = 0
        l = 0
        maxf = 0

        for r in range(len(s)):

            chars[s[r]] = 1 + chars.get(s[r], 0)
            maxf = max(maxf, chars[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1



            output = max(output, r-l+1)

        return output

        
        