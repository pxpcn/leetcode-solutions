class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1

            seen[ch] = right

            max_len = max(max_len, right - left + 1)

        return max_len