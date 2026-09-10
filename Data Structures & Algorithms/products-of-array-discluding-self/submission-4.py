class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use a loop to find the product of nums = result
        # use a new array, and result/nums[i]

        count_zero = 0
        result = 1
        for i in range (len(nums)):
            if nums[i] != 0:
                result = result * nums[i]
            if nums[i] == 0:
                count_zero += 1
                zero_index = i
        
        final = []
        if count_zero == 0:
            for i in range (len(nums)):
                final.append(result // nums[i])
        elif count_zero >= 2:
            for i in range (len(nums)):
                final.append(0)
        else:
            for i in range (len(nums)):
                if nums[i] == 0:
                    final.append(result)
                else:
                    final.append(0)
        
        return final