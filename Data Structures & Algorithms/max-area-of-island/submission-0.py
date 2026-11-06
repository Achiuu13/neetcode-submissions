class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        maxArea = 0

        def dfs(r, c, count):
            if r < 0 or r >= ROW or c < 0 or c >= COL: return count
            if grid[r][c] == 0: return count

            grid[r][c] = 0
            count += 1

            for dr, dc in directions:
                count = dfs(dr + r, dc + c, count)

            return count
        
        for r in range(ROW):
            count = 0
            for c in range(COL):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c, count))
        return maxArea
