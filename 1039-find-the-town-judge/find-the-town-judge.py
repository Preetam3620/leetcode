class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for (k, v) in trust:
            incoming[v] += 1
            outgoing[k] += 1

        for i in range(1, n + 1):
            if incoming[i] == (n - 1) and outgoing[i] == 0:
                return i
        
        return -1