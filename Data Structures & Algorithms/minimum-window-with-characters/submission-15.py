class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        freq_t = {}

        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)

        min_length = 100001
        window = [0,0]
        
        freq_s = {}
        l = 0

        have = 0
        need = len(freq_t)

        for r in range(len(s)):
            freq_s[s[r]] = 1 + freq_s.get(s[r], 0)

            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < min_length:
                    window = [l,r]
                    min_length = (r-l+1)

                freq_s[s[l]] = freq_s.get(s[l], 0) - 1

                if s[l] in freq_t and freq_s[s[r]] < freq_t[s[r]]:
                    have -=1

                l += 1



        return s[window[0]:window[1]]





        

        
        