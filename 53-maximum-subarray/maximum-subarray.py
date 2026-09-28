class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = 0
        maxSum = nums[0]

        for n in nums:
            sum += n
            maxSum = max(maxSum, sum)
            if sum < 0:
                sum = 0 
        
        return maxSum