class Solution:

    def encode(self, strs: List[str]) -> str:
        test = ''

        for word in strs:
            length = len(word)

            test += f'{length}#{word}'

        return test

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            # 1. Read number until '#'
            num_str = ""
            while s[i] != '#':
                num_str += s[i]
                i += 1

            count = int(num_str)

            # 2. Skip '#'
            i += 1

            # 3. Read exactly <count> characters
            word = s[i:i+count]
            result.append(word)

            # 4. Move index forward
            i += count   

        return result 
