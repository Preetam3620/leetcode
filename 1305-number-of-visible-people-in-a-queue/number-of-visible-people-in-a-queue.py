class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []  # monotonic decreasing stack of heights

        for i in range(n - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                ans[i] += 1      # person i sees this shorter person
                stack.pop()      # shorter person gets blocked by i anyway

            if stack:            # first taller person - visible but blocks view
                ans[i] += 1

            stack.append(heights[i])

        return ans