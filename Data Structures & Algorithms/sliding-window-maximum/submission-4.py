class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_heap = []

        left = 0

        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            if right - left + 1 == k:
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                result.append(-max_heap[0][0])
                left += 1
        return result