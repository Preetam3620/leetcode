import copy

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zeroPointer = -1
        # curr = 0
        # while curr < len(nums):
        #     if nums[curr] == 0:
        #         zeroPointer = curr
        #     else:
        #         if zeroPointer == curr:
        #             curr += 1
        #         else:
        #             temp = nums[curr]
        #             nums[curr] = nums[zeroPointer]
        #             nums[zeroPointer] = temp
        #     print(nums)
        arr = [0] * len(nums)
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                arr[k] = nums[i]
                k += 1
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        print(nums, arr)