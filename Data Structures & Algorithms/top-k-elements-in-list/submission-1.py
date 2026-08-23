class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# step 1: get the frequency use dictionary
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

# step 2: put them into a frequcy bucket using a list of lists
        bucket = []
        for i in range (len(nums) + 1):
            bucket.append([])
        
        for num, frequency in count.items():
            bucket[frequency].append(num)

# count backwards, stop at K, render a list
        result = []
        for frequency in range (len(nums), 0, -1):
            for num in bucket[frequency]:
                result.append(num)
                if len(result) == k:
                    return result
