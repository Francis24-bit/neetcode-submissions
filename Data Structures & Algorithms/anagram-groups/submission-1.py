class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

# use frequency array/list to count the frequency of letters in each word.
# same frequency as one key to a dictionary with value = list of words

        group = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1
            
            key = tuple(count)

            if key not in group:
                group[key] = []
            
            group[key].append(word)
        
        return list(group.values())