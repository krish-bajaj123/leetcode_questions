# Last updated: 5/30/2026, 12:37:32 AM
1class MedianFinder:
2    def __init__(self):
3        self.left = []   # max heap (negated)
4        self.right = []  # min heap
5
6    def _push_min(self, heap, val):
7        heap.append(val)
8        i = len(heap) - 1
9        while i > 0:
10            parent = (i - 1) // 2
11            if heap[parent] > heap[i]:
12                heap[parent], heap[i] = heap[i], heap[parent]
13                i = parent
14            else:
15                break
16
17    def _pop_min(self, heap):
18        heap[0], heap[-1] = heap[-1], heap[0]
19        val = heap.pop()
20        i = 0
21        n = len(heap)
22        while True:
23            left, right, smallest = 2*i+1, 2*i+2, i
24            if left < n and heap[left] < heap[smallest]:
25                smallest = left
26            if right < n and heap[right] < heap[smallest]:
27                smallest = right
28            if smallest == i:
29                break
30            heap[i], heap[smallest] = heap[smallest], heap[i]
31            i = smallest
32        return val
33
34    def addNum(self, num: int) -> None:
35        # Push to left (max heap via negation)
36        self._push_min(self.left, -num)
37
38        # Balance values: left max <= right min
39        if self.right and -self.left[0] > self.right[0]:
40            self._push_min(self.right, -self._pop_min(self.left))
41
42        # Balance sizes
43        if len(self.left) > len(self.right) + 1:
44            self._push_min(self.right, -self._pop_min(self.left))
45        elif len(self.right) > len(self.left):
46            self._push_min(self.left, -self._pop_min(self.right))
47
48    def findMedian(self) -> float:
49        if len(self.left) > len(self.right):
50            return float(-self.left[0])
51        return (-self.left[0] + self.right[0]) / 2
52        
53
54
55# Your MedianFinder object will be instantiated and called as such:
56# obj = MedianFinder()
57# obj.addNum(num)
58# param_2 = obj.findMedian()