from typing import Generic, Iterable, List, TypeVar, Hashable

T = TypeVar("T", bound=Hashable)


class Trie(Generic[T]):
    def __init__(self) -> None:
        self.children: dict[T, Trie[T]] = {}
        self.is_end = False

    def insert(self, seq: Iterable[T]):
        node = self
        for e in seq:
            if not e in node.children:
                node.children[e] = Trie()
            node = node.children[e]
        node.is_end = True

    def search(self, seq: Iterable[T]) -> bool:
        node = self
        for e in seq:
            if not e in node.children:
                return False
            node = node.children[e]
        return node.is_end

    def startsWith(self, seq: Iterable[T]) -> bool:
        node = self
        for e in seq:
            if not e in node.children:
                return False
            node = node.children[e]
        return True


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return 0
