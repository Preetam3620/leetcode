class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # precompute factorials
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        nums = list(range(1, n + 1))  # [1,2,3,...,n]
        result = []
        k -= 1  # convert to 0-indexed

        for i in range(n, 0, -1):
            index = k // factorial[i - 1]  # which block
            result.append(str(nums[index]))
            nums.pop(index)               # remove used digit
            k %= factorial[i - 1]         # remainder for next position

        return "".join(result)