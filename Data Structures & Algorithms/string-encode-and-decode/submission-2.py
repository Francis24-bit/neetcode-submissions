class Solution:
#use list + join not + + as every time str +, there is a new str, so use list + join you do not have to copy the string ever time as it is faster
    def encode(self, strs: List[str]) -> str:
        result  = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result 


# the idea is you need to express in one way the numnber(the length of the word, it can be as length = s[i:j] then the word itself is j+1, and end of the word is  j + 1 + length)
    def decode(self, s: str) -> List[str]:
        start = 0
        final = []
        while start < len(s):
            end = s.find("#", start) #find the next "#" from start
            length = int(s[start : end]) # slice anything between start and end and turn it into an integer, which gives you the length of the word
            word = s[end + 1 : end + length + 1]
            final.append(word)
            start = end + length + 1
        
        return final