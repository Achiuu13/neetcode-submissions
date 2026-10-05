class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = {}
        visit = set()
        res = 0
        for i in range(n):
            m[i] = []
        for e in edges:
            m[e[0]].append(e[1])
            m[e[1]].append(e[0])

        def dfs(curr):
            if curr in visit: return
            visit.add(curr)
            for nei in m[curr]:
                dfs(nei)
    
        for node in range(n):
            if node not in visit:
                dfs(node)
                res += 1
        return res