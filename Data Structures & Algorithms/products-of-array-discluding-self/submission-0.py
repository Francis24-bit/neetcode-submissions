class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        count = 0
        for num in nums:
            if num != 0:
                result = result * num
            else:
                count += 1
        
        final = []
        if count == 0:
            for num in nums:
                final.append(result // num)
        
        if count >= 2:
            for num in nums:
                final.append(0 * num)
        
        if count == 1:
            for num in nums:
                if num == 0:
                    final.append(result)
                else:
                    final.append(0)

        return final