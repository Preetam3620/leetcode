class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        q = deque([0])
        visited = set([0])
        n = len(s)
        
        while q:
            start = q.popleft()

            for end in range(start + 1, n + 1):
                if end in visited:
                    continue
                if s[start:end] in words: 
                    if end == n:
                        return True
                    q.append(end)
                    visited.add(end)

        return False