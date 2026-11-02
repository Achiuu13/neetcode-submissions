class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]
        res.append(newInterval)
        return res