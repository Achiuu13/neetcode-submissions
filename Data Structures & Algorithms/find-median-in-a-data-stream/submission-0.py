class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            temp = -self.maxHeap[0]
            heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, temp)
        if abs(len(self.minHeap) - len(self.maxHeap)) >= 2:
            if len(self.minHeap) > len(self.maxHeap):
                temp = self.minHeap[0]
                heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -temp)
            else:
                temp = -self.maxHeap[0]
                heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, temp)

    def findMedian(self) -> float:
        if self.maxHeap and len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        elif self.minHeap and len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        elif self.maxHeap and self.minHeap and len(self.maxHeap) == len(self.minHeap):
            return float((-self.maxHeap[0] + self.minHeap[0]) / 2)
        
        