class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # binary search approach
        arr = [] # builds LIS 
        for num in nums:
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            if left == len(arr):
                arr.append(num)
            else:
                arr[left] = num
        return len(arr)