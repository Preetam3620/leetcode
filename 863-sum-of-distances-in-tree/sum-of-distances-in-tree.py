class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n   # subtree size, starts at 1 (itself)
        ans = [0] * n

        # DFS 1 - post-order: compute count[] and ans[0]
        def dfs1(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue
                
                dfs1(child, node)

                count[node] += count[child]
                ans[node] += ans[child] + count[child]

        # DFS 2 - pre-order: re-root trick to fill ans[]
        def dfs2(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue
                ans[child] = ans[node] - count[child] + (n - count[child])
                dfs2(child, node)

        dfs1(0, -1)

        dfs2(0, -1)
        return ans