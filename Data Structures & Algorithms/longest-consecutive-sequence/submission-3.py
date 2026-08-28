class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use set to remove depulicates
        if nums == []:
            return 0
        seen = set(nums)
        
        final = []
        # loop through the set to see if num - 1 is in the set, unitl it is not
        for num in seen:
            if num - 1 not in seen:
                start = num
            
                current = start
                while current in seen:
                    current += 1
                length = current - start

                final.append(length)

        return max(final)
        # use that as the start, and use a conuter to see when the num is not in the set, and find the length.
        # put length in a list, and max the list

