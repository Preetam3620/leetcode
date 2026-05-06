class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums.sort()
        count = 1
        maxCount = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                count += 1
            elif nums[i + 1] == nums[i]:
                pass
            else:
                maxCount = max(count, maxCount)
                count = 1
        maxCount = max(count, maxCount)
        return maxCount