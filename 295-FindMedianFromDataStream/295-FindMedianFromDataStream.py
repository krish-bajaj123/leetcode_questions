# Last updated: 5/30/2026, 12:37:44 AM
class MedianFinder:
    def __init__(self):
        self.left = []   # max heap (negated)
        self.right = []  # min heap

    def _push_min(self, heap, val):
        heap.append(val)
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if heap[parent] > heap[i]:
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent
            else:
                break

    def _pop_min(self, heap):
        heap[0], heap[-1] = heap[-1], heap[0]
        val = heap.pop()
        i = 0
        n = len(heap)
        while True:
            left, right, smallest = 2*i+1, 2*i+2, i
            if left < n and heap[left] < heap[smallest]:
                smallest = left
            if right < n and heap[right] < heap[smallest]:
                smallest = right
            if smallest == i:
                break
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        return val

    def addNum(self, num: int) -> None:
        # Push to left (max heap via negation)
        self._push_min(self.left, -num)

        # Balance values: left max <= right min
        if self.right and -self.left[0] > self.right[0]:
            self._push_min(self.right, -self._pop_min(self.left))

        # Balance sizes
        if len(self.left) > len(self.right) + 1:
            self._push_min(self.right, -self._pop_min(self.left))
        elif len(self.right) > len(self.left):
            self._push_min(self.left, -self._pop_min(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        return (-self.left[0] + self.right[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()