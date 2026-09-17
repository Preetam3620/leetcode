class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        maxLen = 0
        left, right = 0, 0
        hashSet = set()

        while right < len(s):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[right])
            maxLen = max(maxLen, (right - left + 1))
            right += 1

        return maxLen 