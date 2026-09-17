class Solution:
    def isPalindrome(self, s: str) -> bool:
        # as I need O(1) space, I can not use a new data structure
        # I need 2 pointers, one from the start index 0 and the other from len(s) - 1
        # i firt see whether s[index].isalnum(), if not, I need to mover the pointer.
        #then ses if s.lower() = the other side, if so move the pointer and return true.
        
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True