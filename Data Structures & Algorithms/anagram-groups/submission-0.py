class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupings = []
        anagram_dict = {}

        for word in strs:
            #this sorts the current word in alpha order
            sorted_string = ''.join(sorted(word))

            #make a key of the word in alpha order, so that 
            #future words that are angrams of it match the key when sorted.
            if sorted_string not in anagram_dict:
                #create a new list at that sorted key
                anagram_dict[sorted_string] = []
            #append the word to the key which is that word sorted.
            anagram_dict[sorted_string].append(word)

        for sorted_key in my_dict:
            current_grouping = []

            for word in my_dict[sorted_key]:
                current_grouping.append(word)
            
            groupings.append(current_grouping)

        return groupings
        