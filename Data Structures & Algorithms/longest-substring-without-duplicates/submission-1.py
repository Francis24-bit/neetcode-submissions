class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_length = 0

        for right in range(0, len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # not in seen:
            seen.add(s[right])
            length = right - left + 1
            max_length = max(max_length, length)

        return max_length