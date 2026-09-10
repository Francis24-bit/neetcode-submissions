class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove duplicates:
        seen = set(nums)
        final = 0

        # find the start of the sequence:
        for num in seen:
            if num - 1 not in seen:
                start = num
            
        # count the length of one sequence
                count = 1
                while start + 1 in seen:
                    count += 1
                    start += 1
        
        # there can be multiple sequences, find the longest one 
                if count > final:
                    final = count 
        
        return final