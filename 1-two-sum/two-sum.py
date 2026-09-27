class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[nums[i]] = i