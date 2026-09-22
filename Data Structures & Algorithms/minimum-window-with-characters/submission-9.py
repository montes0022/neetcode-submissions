class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

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

                #pop from the left of our window and move l up!   
                countt[s[l]] -= 1

                #decrementing the value at s[l] may make HAVE and NEED equal.
                if s[l] in counts:
                #if the values of the keys match, HAVE can down 1.
                #since we are moving l up.
                    if countt[s[l]] < counts[s[l]]:
                        HAVE -= 1
                #since we remove a char from the left the count and 
                #window frequency map for s need to be updated.
                #move l up one.
                l += 1

        #extract res and put it inside of l and r
        l, r = res

        #if length has been changed since the beginning, return the spliced s
        if length != float("infinity"):
            #splice s to get from index s to r inclusive
            return s[l:r+1]
        else: #if length is still infinity.
            return ""
        