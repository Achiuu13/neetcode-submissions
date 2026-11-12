class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        m = {}
        for i in range(n):
            m[i] = []
        for u, v, price in flights:
            m[u].append((v, price))
        minPrice = float('inf')
        visited = {}
        def dfs(src, cost, stops):
            nonlocal minPrice
            if (src, stops) in visited:
                if cost >= visited[(src, stops)]:
                    return float('inf')
            visited[(src, stops)] = cost
            if cost >= minPrice:
                return float('inf')
            if stops > k + 1:
                return float('inf')
            if src == dst and stops <= k + 1:
                return cost
            for dest, price in m[src]:
                minPrice = min(minPrice, dfs(dest, cost + price, stops + 1))
            return minPrice
        res = dfs(src, 0, 0)
        return res if res != float('inf') else -1