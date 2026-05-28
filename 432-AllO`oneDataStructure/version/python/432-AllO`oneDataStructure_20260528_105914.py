# Last updated: 5/28/2026, 10:59:14 AM
1class AllOne:
2
3    class Node:
4        """A doubly linked list node holding all keys with the same count."""
5        def __init__(self, count=0):
6            self.count = count
7            self.keys = set()       # All keys at this count level
8            self.prev = None
9            self.next = None
10
11    def __init__(self):
12        # Sentinel head (min side) and tail (max side)
13        self.head = self.Node(0)        # Guard: before all real nodes
14        self.tail = self.Node(float('inf'))  # Guard: after all real nodes
15        self.head.next = self.tail
16        self.tail.prev = self.head
17
18        self.key_map = {}    # key  -> Node (which count-level node it lives in)
19        self.count_map = {}  # count -> Node (the node for that count value)
20    def _insert_after(self, node: 'AllOne.Node', new_node: 'AllOne.Node'):
21        """Insert new_node immediately after node."""
22        new_node.prev = node
23        new_node.next = node.next
24        node.next.prev = new_node
25        node.next = new_node
26
27    def _remove_node(self, node: 'AllOne.Node'):
28        """Unlink node from the list and drop it from count_map."""
29        node.prev.next = node.next
30        node.next.prev = node.prev
31        del self.count_map[node.count]
32
33    def _get_or_create_node(self, count: int, insert_after: 'AllOne.Node') -> 'AllOne.Node':
34        """
35        Return the node for `count`, creating and linking it after
36        `insert_after` if it doesn't exist yet.
37        """
38        if count not in self.count_map:
39            new_node = self.Node(count)
40            self._insert_after(insert_after, new_node)
41            self.count_map[count] = new_node
42        return self.count_map[count]
43    
44        
45
46    def inc(self, key: str) -> None:
47        if key not in self.key_map:
48            # New key: place at count=1 (right after sentinel head)
49            node = self._get_or_create_node(1, self.head)
50            node.keys.add(key)
51            self.key_map[key] = node
52        else:
53            cur_node = self.key_map[key]
54            new_count = cur_node.count + 1
55
56            # Get or create the node for new_count, placed after cur_node
57            new_node = self._get_or_create_node(new_count, cur_node)
58            new_node.keys.add(key)
59            self.key_map[key] = new_node
60
61            # Remove key from old node; clean up if empty
62            cur_node.keys.discard(key)
63            if not cur_node.keys:
64                self._remove_node(cur_node)
65
66    def dec(self, key: str) -> None:
67        cur_node = self.key_map[key]
68        new_count = cur_node.count - 1
69
70        if new_count == 0:
71            del self.key_map[key]
72        else:
73            # Move key to the node for (count-1), placed before cur_node
74            new_node = self._get_or_create_node(new_count, cur_node.prev)
75            new_node.keys.add(key)
76            self.key_map[key] = new_node
77
78        # Remove key from old node; clean up if empty
79        cur_node.keys.discard(key)
80        if not cur_node.keys:
81            self._remove_node(cur_node)
82
83    def getMaxKey(self) -> str:
84        if self.tail.prev is self.head:  # List is empty
85            return ""
86        return next(iter(self.tail.prev.keys))
87
88    def getMinKey(self) -> str:
89        if self.head.next is self.tail:  # List is empty
90            return ""
91        return next(iter(self.head.next.keys))
92        
93
94
95# Your AllOne object will be instantiated and called as such:
96# obj = AllOne()
97# obj.inc(key)
98# obj.dec(key)
99# param_3 = obj.getMaxKey()
100# param_4 = obj.getMinKey()