class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        curNum = n
        while(True):
            if curNum == 1:
                return True
            if curNum in arr:
                return False

            arr.append(curNum)
            total = 0
            while curNum > 0:
                digit = curNum % 10
                total += digit ** 2
                curNum = curNum // 10
            curNum = total 