class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count1 = {}
        count2 = {}

        for j in range(0, len(s1)):
            if s1[j] not in count1:
                count1[s1[j]] = 0
            count1[s1[j]] += 1

        for i in range (0, len(s2)):
            if s2[i] not in count2:
                count2[s2[i]] = 0
            count2[s2[i]] += 1

            while i - left + 1 > len(s1):
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1

            if i - left + 1 == len(s1) and count1 == count2:
                return True
        
        return False