class Solution:
    def isValid(self, s: str) -> bool:
        book = { ")" : "(",
                "]" : "[",
                "}" : "{"
        }

        store = []

        for letter in s:
            if letter in "([{":
                store.append(letter)
            
            if letter in ")]}":
                if not store:
                    return False
                elif store[-1] == book[letter]:
                    store.pop()
                else:
                    return False
        if store:
            return False
        return True