class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        numIslands = 0
        visit = set()
        def dfs(r, c, visit):
            if r >= len(grid) or c >= len(grid[0]): return
            if min(r,c) < 0: return
            if grid[r][c] == "0": return
            if (r,c) in visit: return

            visit.add((r,c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visit)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    numIslands += 1
                    dfs(i, j, visit)
        return numIslands