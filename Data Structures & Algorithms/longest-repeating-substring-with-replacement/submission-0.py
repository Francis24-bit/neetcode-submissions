class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        left = 0
        count = {}

        for i in range(0, len(s)):
            if s[i] not in count:
                count[s[i]] = 0
            count[s[i]] += 1
            most_repeat = max(count.values())

            while((i - left + 1) - most_repeat) > k:
                count[s[left]] -= 1
                left += 1
                most_repeat = max(count.values())
            length = max(length, i - left + 1)

        return length