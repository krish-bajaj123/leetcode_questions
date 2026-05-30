# Last updated: 5/30/2026, 12:37:45 AM
class AllOne:

    class Node:
        """A doubly linked list node holding all keys with the same count."""
        def __init__(self, count=0):
            self.count = count
            self.keys = set()       # All keys at this count level
            self.prev = None
            self.next = None

    def __init__(self):
        # Sentinel head (min side) and tail (max side)
        self.head = self.Node(0)        # Guard: before all real nodes
        self.tail = self.Node(float('inf'))  # Guard: after all real nodes
        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_map = {}    # key  -> Node (which count-level node it lives in)
        self.count_map = {}  # count -> Node (the node for that count value)
    def _insert_after(self, node: 'AllOne.Node', new_node: 'AllOne.Node'):
        """Insert new_node immediately after node."""
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove_node(self, node: 'AllOne.Node'):
        """Unlink node from the list and drop it from count_map."""
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_map[node.count]

    def _get_or_create_node(self, count: int, insert_after: 'AllOne.Node') -> 'AllOne.Node':
        """
        Return the node for `count`, creating and linking it after
        `insert_after` if it doesn't exist yet.
        """
        if count not in self.count_map:
            new_node = self.Node(count)
            self._insert_after(insert_after, new_node)
            self.count_map[count] = new_node
        return self.count_map[count]
    
        

    def inc(self, key: str) -> None:
        if key not in self.key_map:
            # New key: place at count=1 (right after sentinel head)
            node = self._get_or_create_node(1, self.head)
            node.keys.add(key)
            self.key_map[key] = node
        else:
            cur_node = self.key_map[key]
            new_count = cur_node.count + 1

            # Get or create the node for new_count, placed after cur_node
            new_node = self._get_or_create_node(new_count, cur_node)
            new_node.keys.add(key)
            self.key_map[key] = new_node

            # Remove key from old node; clean up if empty
            cur_node.keys.discard(key)
            if not cur_node.keys:
                self._remove_node(cur_node)

    def dec(self, key: str) -> None:
        cur_node = self.key_map[key]
        new_count = cur_node.count - 1

        if new_count == 0:
            del self.key_map[key]
        else:
            # Move key to the node for (count-1), placed before cur_node
            new_node = self._get_or_create_node(new_count, cur_node.prev)
            new_node.keys.add(key)
            self.key_map[key] = new_node

        # Remove key from old node; clean up if empty
        cur_node.keys.discard(key)
        if not cur_node.keys:
            self._remove_node(cur_node)

    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:  # List is empty
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:  # List is empty
            return ""
        return next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()