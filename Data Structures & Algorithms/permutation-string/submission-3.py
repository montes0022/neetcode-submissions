class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        matches = 0

        #init the "hashmap" of s1count and s2count by looping thru s1
        #if s1 is 3 chars long, we would look at first 3 characters of s2
        for i in range(len(s1)):
            #geting ascii value of the item at i inside s1 will give us 
            #a index at s1 couunt, subtract this by ascii value of a
            #ascii values of a-z are in order 97-122, so this difference will
            #always be within 26.
            #for both s1Count and s2count, and their respective strings,
            #monitor the frequency of the window where the window size
            #is all of s1.
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            #only increment matches if s1Count and s2Count at position i are 
            #matching. The items at position i represent the frequency.
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0

        #we already have the windows initialized with s1Count and s2Count
        #so we start at the length of s1 and iterate thru the rest of s2
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            #this character at r will be added to our window
            #increment the frequency of this character by one in s2Count
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            #since we just added this to the s2Count, doing s2Count[i] +=1
            #lets see if this frequency matches the frequency of the 
            #character in s1
            #if the frequency matches after addition
            if s1Count[index] == s2Count[index]:
                matches += 1
            #by adding 1 to s2Count[index], we also could have made it bigger by
            #one.
            #this means the frequencies were equal until the add.
            #this means they do not match so matches goes down one.
            elif s1Count[index] + 1 == s2Count[index]:
                matches -=1

            #OPPOSITE FROM CHUNK ABOVE
            #this character at l will be removed to our window
            #decrement the frequency of this character by one in s2Count
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            #since we just removed this from the s2Count, doing s2Count[i]-+=1
            #lets see if this frequency matches the frequency of the 
            #character in s1
            #if the frequency matches after subtraction
            if s1Count[index] == s2Count[index]:
                matches += 1
            #by removing 1 from s2Count[index], we also 
            #could have made it bigger by one.
            #this means the frequencies were equal until the subtraction.
            #this means they do not match so matches goes down one.
            elif s1Count[index] - 1 == s2Count[index]:
                matches -=1
        #after loop see if matches is 26
        return matches == 26


