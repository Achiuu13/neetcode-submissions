class TrieNode:
    def __init__(self):
        self.m = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.m:
                    curr.m[c] = TrieNode()
                curr = curr.m[c]
            curr.end = True
        
        ROW, COL = len(board), len(board[0])
        directions = [[0, 1],[0, -1],[1,0],[-1,0]]
        res = set()
        visited = set()

        def dfs(r, c, node, word):
            if r < 0 or r >= ROW or c < 0 or c >= COL: return
            if (r, c) in visited: return
            if board[r][c] not in node.m: return

            visited.add((r, c))
            node = node.m[board[r][c]]
            word += (board[r][c])

            if node.end:
                res.add(word)
            for dr, dc in directions:
                dfs(dr + r, dc + c, node, word)
            visited.remove((r, c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, "")
        return list(res)