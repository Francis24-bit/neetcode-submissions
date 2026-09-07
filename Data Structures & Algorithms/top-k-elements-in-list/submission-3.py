class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        
        for num, frequency in count.items():
            bucket[frequency].append(num)

        final = []  
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                final.append(num)
                if len(final) == k:
                        return final
