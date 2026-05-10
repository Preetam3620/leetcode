class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        visited.add(source)

        def dfs(i):
            if i == destination:
                return True

            for neib_node in graph[i]:
                if neib_node not in visited:
                    visited.add(neib_node)
                    if dfs(neib_node):
                        return True

            return False

        return dfs(source)