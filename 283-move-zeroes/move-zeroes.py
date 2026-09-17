class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0
        for index, num in enumerate(nums):
            if num != 0:
                nums[index], nums[nonZeroIndex] = nums[nonZeroIndex], nums[index]
                nonZeroIndex += 1