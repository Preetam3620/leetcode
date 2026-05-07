class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)

        freqArr = [[] for i in range(len(nums) + 1)]

        # storing nums at index - count
        for num, count in freqMap.items():
            freqArr[count].append(num)
        print(freqArr)

        # reverse iterating over freqArr, getting k elements
        result = []
        for i in range(len(freqArr) - 1, 0, -1):
            for n in freqArr[i]:
                result.append(n)
                if len(result) == k:
                    return result