class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''

        for word in strs:
            length = len(word)
            res += f'{length}%{word}'

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        #can also set i = 0 and do a while loop while i < len(s)
        for i in range(len(s)):
            count_string = ''
            while s[i] != '%':
                count_string += s[i]

            count_int = int(count_string)

            i += 1

            #if the word started at s[2] and the count_int was 5->
            #the range of the word in s would be s[2] to s[7], but->
            #splicing is non inclusive at the end so really would be at
            #s[2] to s[6], a word of 5 characters.
            word = s[i: i+count_int]
            res.append(word)

            i+= count_int

        return res




        
