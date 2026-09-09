class Solution:

    def encode(self, strs: List[str]) -> str:
        result  = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

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