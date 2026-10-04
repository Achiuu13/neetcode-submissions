class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(board, r, c, i, visit):
            if i == len(word): return True
            if min(r, c) < 0: return False
            if r >= ROWS or c >= COLS: return False
            if board[r][c] != word[i]: return False
            if (r,c) in visit: return False

            visit.add((r,c))
            found = (dfs(board, r + 1, c, i + 1, visit) or
            dfs(board, r - 1, c, i + 1, visit) or
            dfs(board, r, c + 1, i + 1, visit) or
            dfs(board, r, c - 1, i + 1, visit))
            visit.remove((r,c))
            return found
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (dfs(board, i, j, 0, set())):
                    return True
                else:
                    continue
        return False
            