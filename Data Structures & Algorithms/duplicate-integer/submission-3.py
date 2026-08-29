class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set up a new set,
        # loop through the list and if num seen, then return true, if not add to the list

        final = set()

        for num in nums:
            if num in final:
                return True
            final.add(num)
        
        return False

