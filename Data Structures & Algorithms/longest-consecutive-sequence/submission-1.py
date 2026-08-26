class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set(nums)
        count = set()

        for num in seen:
            if num - 1 not in seen:
                start = num

                current = start
                while current + 1 in seen:
                    current += 1
            
                length = current - start + 1
                count.add(length)
        
        return max(count)