class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_heap = []
        window = deque()

        left = 0

        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            window.append((nums[right], right))
            if right - left + 1 == k:
                result.append(-max_heap[0][0])
                old_value, old_index = window.popleft()
                max_heap.remove((-old_value, old_index))
                heapq.heapify(max_heap)
                left += 1
        return result