class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        output = ""
        res = [0,0]
        length = float("infinity")
        #do we need to keep track of the frequencies of the 
        #characters in t?
        #frequency map for t
        counts = {}
        #frequency map for window iterating over the s string.
        countt = {}
  
        for i in range(len(t)):
            counts[t[i]] = 1 + counts.get(t[i], 0)

        NEED = len(counts)
        HAVE = 0

        l = 0
        for r in range(len(s)):

            #addon s2[r] letter key to dict and append frequency
            #addon frequency of s[r] to countt
            #this dict represents what we have
            #counts dict represents what we at least need in countt
            countt[s[r]] = 1 + countt.get(s[r], 0)

            #check if what we added is in counts
            if s[r] in counts:
                #if the values of the keys match, HAVE can go up 1.
                if countt[s[r]] == counts[s[r]]:
                    HAVE += 1

            
            if HAVE == NEED:
                res = [l, r]
                length = r - l + 1

            #do we have what we need?
            #if so, the substring we have looked at so far has the characters
            #needed from string t.
            #why is this a loop over an if statement like i wrote?

            while HAVE == NEED:
                #update your result.
                #since length is set to infinity, this will execute at some point
                #r-l+1 is our current window size!
                #it gets updated with the smaller size, and r and l are updated.
                if (r-l+1) < length:
                    res = [l,r]
                    length = (r-l+1)
                countt[s[l]] = countt.get(s[l], 0) - 1

                if countt[s[l]] == counts[s[l]]:
                    HAVE -= 1

    

            




        #the output will at least be the length of s
        if len(output) == 0:
            return ""
        else:
            return s[l:r]
        