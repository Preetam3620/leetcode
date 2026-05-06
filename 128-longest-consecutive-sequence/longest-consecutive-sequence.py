class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        numSet = set(nums)
        longest = 1
        for n in numSet:
            if n - 1 not in numSet:
                count = 1
                start = n
                while start + 1 in numSet:
                    start += 1
                    count += 1
                longest = max(longest, count)

        return longest