class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use a loop to find the product of nums = result
        # use a new array, and result/nums[i]

        count_zero = 0
        result = 1
        for i in range (len(nums)):
            if nums[i] != 0:
                result = result * nums[i]
            else:
                count_zero += 1
        
        final = []
        for i in range (len(nums)):
            if count_zero == 0:
                final.append(result // nums[i])
            elif count_zero >= 2:
                final.append(0)
            else:
                if nums[i] == 0:
                    final.append(result)
                else:
                    final.append(0)
        return final