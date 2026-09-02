class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        book = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for letter in s:
            if letter in "({[":
                stack.append(letter)
            elif stack and stack [-1] == book[letter]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False