class Solution:
    def isPalindrome(self, s: str) -> bool:
        #from the internet, clean off all non-alphanumeric characters from s
        print(s)
        cleaned_string = ''.join(char for char in s if char.isalnum())
        print(cleaned_string)
        start = 0
        end = len(cleaned_string)-1

        while start <= end:
            if cleaned_string[start].lower() != cleaned_string[end].lower():
                return False
            start += 1
            end -= 1

        return True