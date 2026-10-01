class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                area = width * height
                res = max(res, area)
                start = index
            stack.append((start, h))

        for start, height in stack:
            width = len(heights) - start
            area = width * height
            res = max(res, area)
        return res