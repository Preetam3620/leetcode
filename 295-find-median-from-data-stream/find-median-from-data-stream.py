from bisect import insort

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        insort(self.arr, num)

    def findMedian(self) -> float:
        arrLen = len(self.arr)
        if arrLen % 2 != 0:
            medianIndex = arrLen // 2
            return self.arr[medianIndex]
        else:
            m1 = arrLen // 2
            m2 = arrLen // 2 - 1
            return (self.arr[m1] + self.arr[m2]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()