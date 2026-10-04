class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        ROWS, COLS = len(heights), len(heights[0])
        aVisit, pVisit = set(), set()
        res = []
        def dfs(r, c, ocean, prev_h):
            if r < 0 or c < 0: return
            if r >= ROWS or c >= COLS: return
            if (r, c) in ocean: return
            if heights[r][c] < prev_h: return

            ocean.add((r,c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, ocean, heights[r][c])
            
        for c in range(COLS):
            dfs(0, c, pVisit, heights[0][c])
            dfs(ROWS - 1, c, aVisit, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, pVisit, heights[r][0])
            dfs(r, COLS - 1, aVisit, heights[r][COLS - 1])
        
       

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pVisit and (r,c) in aVisit:
                    res.append([r,c])
        return res