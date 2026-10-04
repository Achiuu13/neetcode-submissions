class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visit = set()
        def dfs(grid, r, c, visit):
            if r >= len(grid) or c >= len(grid[0]): return
            if min(r,c) < 0: return
            if grid[r][c] == "0": return
            if (r,c) in visit: return

            visit.add((r,c))

            dfs(grid, r  + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c - 1, visit)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    numIslands += 1
                    dfs(grid, i, j, visit)
        return numIslands