class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                row = matrix[m]
                l, r = 0, len(row) - 1
                while l <= r:
                    m = (l + r) // 2

                    if target < row[m]:
                        r = m - 1
                    elif target > row[m]:
                        l = m + 1
                    else:
                        return True
                return False
        return False