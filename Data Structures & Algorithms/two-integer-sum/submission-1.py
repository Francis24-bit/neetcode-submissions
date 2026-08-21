class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for index, num in enumerate(nums):
            need = target - num

            if need in dict1:
                return [dict1[need], index]

            dict1[num] = index
        
