from typing import Dict, Optional

class Node:
    """A node representing a key-value pair in the doubly linked list."""
    def __init__(self, key: int, value: int):
        self.key: int = key
        self.value: int = value
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class LRUCache:
    """
    Least Recently Used (LRU) Cache implementation.
    Utilizes a Hash Map and a Doubly Linked List to achieve O(1) operations.
    """
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: Dict[int, Node] = {}
        
        self.head: Node = Node(0, 0)
        self.tail: Node = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Removes an existing node from the linked list."""
        p = node.prev
        n = node.next
        if p is not None and n is not None:
            p.next = n
            n.prev = p

    def _add_to_head(self, node: Node) -> None:
        """Inserts a node right after the dummy head."""
        node.prev = self.head
        node.next = self.head.next
        
        nxt = self.head.next
        if nxt is not None:
            nxt.prev = node
            
        self.head.next = node

    def get(self, key: int) -> int:
        """Returns the value of the key if it exists, otherwise -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Adds or updates a key-value pair, evicting the LRU item if at capacity."""
        if key in self.cache:
            self._remove(self.cache[key])
        
        new_node = Node(key, value)
        self._add_to_head(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            if lru_node is not None and lru_node is not self.head:
                self._remove(lru_node)
                self.cache.pop(lru_node.key, None)