class Solution:
    def isPalindrome(self, s: str) -> bool:
        #from the internet, clean off all non-alphanumeric characters from s
        cleaned_string = ''.join(char for char in s if char.isalnum())
        start = 0
        end = len(cleaned_string)-1

        while start <= end:
            if cleaned_string[start] != cleaned_string[end]:
                return False
            start += 1
            end -= 1

        return True