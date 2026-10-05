class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = {}
        visit = set()
        for node in range(n):
            m[node] = []
        for e in edges:
            m[e[0]].append(e[1])
            m[e[1]].append(e[0])
        def dfs(curr, prev):
            if curr in visit: return False
            visit.add(curr)
            for nei in m[curr]:
                if nei == prev:
                    continue
                else:
                    if not dfs(nei, curr):
                        return False
            return True
        if not dfs(0, -1):
            return False
        if len(visit) == n:
            return True
        return False