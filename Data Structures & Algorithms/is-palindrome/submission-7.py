class Solution:
    def isPalindrome(self, s: str) -> bool:
        #from the internet, clean off all non-alphanumeric characters from s
        c_s = ''.join(char for char in s if char.isalnum())
        print(c_s)
        start = 0
        end = len(c_s) - 1

        while start <= end:
            if c_s[start] == c_s[end]:
                print(c_s[start])
                print(c_s[end])
                start += 1
                end -= 1
            else:
                return False


        return True

