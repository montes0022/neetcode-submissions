class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = len(s1)
        ordred = ''.join(sorted(s1))

        for l in range(len(s2)):
            chunk = s2[l:l+window]

            if ''.join(sorted(chunk)) == ordered:
                return True
                
        return False
        