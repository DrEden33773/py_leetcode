from queue import PriorityQueue


class Accumulation:
    def __init__(self, cost=0.0, dst=0) -> None:
        self.cost = cost
        self.dst = dst

    def __lt__(self, other: "Accumulation") -> bool:
        return self.cost > other.cost

    def __eq__(self, other: "Accumulation") -> bool:
        return self.cost == other.cost


class Solution:
    def buildAdjList(
        self,
        n: int,
        edges: list[list[int]],
        succ_prob: list[float],
    ) -> list[list[tuple[float, int]]]:
        adj_list = [[] for _ in range(n)]
        for (src, dst), prob in zip(edges, succ_prob):
            adj_list[src].append((prob, dst))
            adj_list[dst].append((prob, src))
        return adj_list

    def dijkstra(
        self,
        adj_list: list[list[tuple[float, int]]],
        start_node: int,
        end_node: int,
    ) -> float:
        prob = [0.0] * len(adj_list)
        heap = PriorityQueue[Accumulation]()

        prob[start_node] = 1.0
        heap.put(Accumulation(1.0, start_node))

        while not heap.empty():
            acc = heap.get()
            startToPicked, picked = acc.cost, acc.dst
            if picked == end_node:
                return startToPicked
            if startToPicked < prob[picked]:
                continue
            for pickedToNew, new in adj_list[picked]:
                startToNew = startToPicked * pickedToNew
                if startToNew > prob[new]:
                    prob[new] = startToNew
                    heap.put(Accumulation(startToNew, new))

        return 0.0

    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succ_prob: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj_list = self.buildAdjList(n, edges, succ_prob)
        return self.dijkstra(adj_list, start_node, end_node)
