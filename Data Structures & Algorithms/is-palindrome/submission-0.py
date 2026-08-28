class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set up a cleaned string without all space and puncuation
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        # 2 pointers, from the start and the end, compare and return true if same
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True