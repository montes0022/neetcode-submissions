class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0
        window = 0
    
        for r in range(len(s)):
            if s[r] in chars:
                chars[s[r]] += 1
            else:
                chars[s[r]] = 1
            max_value = max(chars.values())
            current_window = ((r-l) + 1)
    
            #if our number of replacements ever exceeds k, move l over.
            #Then the window is valid — you can make all characters 
            #identical with ≤ k repl acements.
            #If it’s not valid, you shrink the window from the left.
            replacements = current_window - max_value
    
            if k < replacements:
                chars[s[l]] -= 1
                l += 1
                current_window = ((r-l) + 1)
            
            window = max(window, current_window)
        return window  
        
        