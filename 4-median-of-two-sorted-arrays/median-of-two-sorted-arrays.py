class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        resultLen = m + n
        
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        # fill leftover
        result.extend(nums1[i:])      
        result.extend(nums2[j:])      
        
        if resultLen % 2 != 0:
            medianIndex = resultLen // 2
            return result[medianIndex]
        else:
            m1 = resultLen // 2
            m2 = resultLen // 2 - 1
            return (result[m1] + result[m2]) / 2