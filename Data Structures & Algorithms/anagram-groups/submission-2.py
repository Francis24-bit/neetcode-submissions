class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

# use frequency array/list to count the frequency of letters in each word.
# same frequency as one key to a dictionary with value = list of words

        group = {}

        #count the frequeny of each word, change them into a tuple as tuple       can not be modified
        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1
            
            key = tuple(count)

# put words with the same key in the dictionary, if key not in the dict, add 
            if key not in group:
                group[key] = []
            
            group[key].append(word)
        
        return list(group.values())