class Solution:

    def encode(self, strs: List[str]) -> str:
        final = []
        for word in strs:
            final.append(str(len(word)) + "#" + word)
        
        return "".join(final)

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            start = j + 1
            end = start + length
            final.append(s[start : end])
            i = end
        
        return final