class Solution:
    def encode(self, strs: List[str]) -> str:
        #init empty string 
        result = ''
        #for each word in the list of strings strs, compute the length of the 
        #word itself. Append it to result, followed by our delimiter '#' then->
        #the actual word.
        for word in strs:
            length = len(word)
            result += f'{length}#{word}'

        #return result.
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        #s passed in would look something like in parenthesis
        #(NUM#helloNUM#world)
        #where NUM is the length of the string between each # and NUM
        #so 5#hello5#world
        while i < len(s):
            #Read number until '#' and assign it to num_str using a while loop.
            num_str = ""
            while s[i] != '#':
                #keep appending the number to num_str
                num_str += s[i]
                i += 1

            #parse the num_str into an integer
            count = int(num_str)

            #Skip over the '#' so that i starts at the first letter of the word.
            i += 1

            #Read exactly 'count' of characters, so i to i+count
            #5#hello5#world
            #s[2] would be h and would go to s[7] (2+5 = 7, 5 because that is->
            #length of hello)
            #do not include s[7] because the split is non inclusive.
            word = s[i:i+count]
            #add the range of characters to a word and then add it to result.
            result.append(word)

            #Move i forward by count so we can start looking at the next number.
            i += count   

        return result 
