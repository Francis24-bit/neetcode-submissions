class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use dict, put the 1st tring in the dict, and count
        # put the 2nd string in the dict and -count
        # check the value
        count = {}
        for letter in s:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
        
        for letter in t:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = -1
        
        for value in count.values():
            if value != 0:
                return False
        
        return True