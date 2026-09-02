class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # set up a dictionary
        # in the form of {key = number, value = index}
        # if find the number, check the index, if in, return, if not, add the number: index
        book = {}

        for index, num in enumerate(nums):
            need = target - num

            if need in book:
                return [book[need], index]
            
            book[num] = index