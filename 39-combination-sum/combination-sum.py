class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            currSum = 0
            for n in subset:
                currSum += n

            if currSum == target:
                res.append(subset.copy())
                return
            
            if i >= len(candidates) or currSum >= target:
                return

            # decision to include candidates[i]
            subset.append(candidates[i])
            dfs(i)

            # decision NOT to include candidates[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res