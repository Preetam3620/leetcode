class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_given = [0] * (n + 1)   # how many people this person trusts
        trust_received = [0] * (n + 1) # how many people trust this person

        for a, b in trust:
            trust_given[a] += 1
            trust_received[b] += 1

        print(trust_given, trust_received)

        for i in range(1, n + 1):
            if trust_given[i] == 0 and trust_received[i] == n - 1:
                return i

        return -1