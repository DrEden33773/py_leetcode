from typing import Optional


class Node:
    def __init__(
        self, val: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None
    ):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def __init__(self) -> None:
        self.cached_node: dict[Node, Node] = {}

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        if not head in self.cached_node:
            headNew = Node(head.val)
            self.cached_node[head] = headNew
            headNew.next = self.copyRandomList(head.next)
            headNew.random = self.copyRandomList(head.random)
        return self.cached_node[head]
