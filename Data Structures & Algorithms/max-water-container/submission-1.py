class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        currMax = 0

        while i < j:
            area = (j - i) * min(heights[i],heights[j])
            currMax = max(area,currMax)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return currMax