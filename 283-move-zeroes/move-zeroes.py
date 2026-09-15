import copy

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[curr], nums[nonZeroIndex] = nums[nonZeroIndex], nums[curr]
                nonZeroIndex += 1
