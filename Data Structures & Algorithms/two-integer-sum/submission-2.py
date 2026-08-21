class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a dictionary to record num and its index like dict[num] = index
        # loop through the list and if the need = target - num is in the list
        # return the index of the num and the index of the need
        # if not, then put the num in the dictionary for future reference

        dict1 = {}

        for index, num in enumerate(nums):
            need = target - num

            if need in dict1:
                return [dict1[need], index]
            
            dict1[num] = index