class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == '.':
                    continue
                boxIndex = (i //3) * 3 + (j // 3)
                if digit in rows[i] or digit in cols[j] or digit in boxes[boxIndex]:
                    return False
                else:
                    rows[i].add(digit)
                    cols[j].add(digit)
                    boxes[boxIndex].add(digit)
        return True