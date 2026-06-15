# Last updated: 6/15/2026, 2:06:45 PM
import bisect

class SummaryRanges:
    def __init__(self):
        self.intervals = []  # list of [start, end], sorted by start

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        # Find insertion point based on start values
        i = bisect.bisect_left(intervals, [value])

        # Check if value is already covered by the previous interval
        if i > 0 and intervals[i-1][1] >= value:
            return  # already in some interval

        # Check if value is already covered by the interval at i (edge case: value == start)
        if i < len(intervals) and intervals[i][0] <= value <= intervals[i][1]:
            return

        # Determine if value connects to previous interval (end + 1 == value)
        merge_left = i > 0 and intervals[i-1][1] + 1 == value
        # Determine if value connects to next interval (start - 1 == value)
        merge_right = i < len(intervals) and intervals[i][0] - 1 == value

        if merge_left and merge_right:
            # Merge previous and next intervals together
            intervals[i-1][1] = intervals[i][1]
            intervals.pop(i)
        elif merge_left:
            intervals[i-1][1] = value
        elif merge_right:
            intervals[i][0] = value
        else:
            intervals.insert(i, [value, value])

    def getIntervals(self):
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()