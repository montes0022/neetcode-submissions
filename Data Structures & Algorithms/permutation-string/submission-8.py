class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS = {}
        countT = {}

        for i in range(len(s1)):
            #always add 1 to the key of every letter that appears in each string
            countS[s1[i]] = 1 + countS.get(s1[i], 0)
            countT[s2[i]] = 1 + countT.get(s2[i], 0)
        
        l = 0

        for r in range(len(s1), len(s2)):
            if countS == countT:
                return True

            countT[s2[r]] = 1 + countT.get(s2[r], 0)

            if countS == countT:
                return True

            countT[s2[l]] = countT.get(s2[l], 0) - 1

            if countS == countT:
                return True

            l += 1

        return countS == countT





        

        

        
        


