from Utils.list import DoubleListNode

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.mru = DoubleListNode(0)
        self.lru = DoubleListNode(-1)

        self.mru.right = self.lru
        self.lru.left = self.mru

    def _append_to_start(self, node: DoubleListNode) -> None:
        node.right = self.mru.right
        node.left = self.mru

        self.mru.right.left = node
        self.mru.right = node

    def _slice_out(self, node: DoubleListNode) -> None:
        node.left.right = node.right
        node.right.left = node.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, node = self.cache[key]

        self._slice_out(node)
        self._append_to_start(node)

        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            evict_key = self.lru.left.value
            self.cache.pop(evict_key)
            self._slice_out(self.lru.left)

        if key in self.cache:
            node = self.cache[key][1]
            self._slice_out(node)
        else:
            node = DoubleListNode(key)

        self._append_to_start(node)

        self.cache[key] = (value, node)