class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        left, right = 0, 0
        result = 0
        charSet = set()
        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            result = max(result, right - left + 1)
            right += 1
        return result