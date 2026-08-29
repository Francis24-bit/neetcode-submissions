class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use dictionary

        book1 = {}
        for char in s:
            if char not in book1:
                book1[char] = 0
            book1[char] += 1

        book2 = {}
        for char in t:
            if char not in book2:
                book2[char] = 0
            book2[char] += 1
        
        return book1 == book2