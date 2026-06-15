# Last updated: 6/15/2026, 2:06:16 PM
1import bisect
2
3class SummaryRanges:
4    def __init__(self):
5        self.intervals = []  # list of [start, end], sorted by start
6
7    def addNum(self, value: int) -> None:
8        intervals = self.intervals
9        # Find insertion point based on start values
10        i = bisect.bisect_left(intervals, [value])
11
12        # Check if value is already covered by the previous interval
13        if i > 0 and intervals[i-1][1] >= value:
14            return  # already in some interval
15
16        # Check if value is already covered by the interval at i (edge case: value == start)
17        if i < len(intervals) and intervals[i][0] <= value <= intervals[i][1]:
18            return
19
20        # Determine if value connects to previous interval (end + 1 == value)
21        merge_left = i > 0 and intervals[i-1][1] + 1 == value
22        # Determine if value connects to next interval (start - 1 == value)
23        merge_right = i < len(intervals) and intervals[i][0] - 1 == value
24
25        if merge_left and merge_right:
26            # Merge previous and next intervals together
27            intervals[i-1][1] = intervals[i][1]
28            intervals.pop(i)
29        elif merge_left:
30            intervals[i-1][1] = value
31        elif merge_right:
32            intervals[i][0] = value
33        else:
34            intervals.insert(i, [value, value])
35
36    def getIntervals(self):
37        return self.intervals
38        
39
40
41# Your SummaryRanges object will be instantiated and called as such:
42# obj = SummaryRanges()
43# obj.addNum(value)
44# param_2 = obj.getIntervals()