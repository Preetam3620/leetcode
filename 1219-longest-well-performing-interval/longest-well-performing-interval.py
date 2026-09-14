class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        first_occurrence = {}
        score = 0
        ans = 0

        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1

            if score > 0:
                ans = i + 1
            else:
                if score - 1 in first_occurrence:
                    ans = max(ans, i - first_occurrence[score - 1])

            if score not in first_occurrence:
                first_occurrence[score] = i

        return ans
