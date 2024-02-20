from math import isqrt
from typing import List


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        X, Y = len(mat), len(mat[0])
        primeCnt = {}

        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for i in range(2, isqrt(n) + 1):
                if n % i == 0:
                    return False
            return True

        def walk_from(x: int, y: int, dx: int, dy: int):
            last = mat[x][y]  # mat[x][y] < 10
            x += dx
            y += dy

            while 0 <= x < X and 0 <= y < Y:
                curr = last * 10 + mat[x][y]
                if curr in primeCnt:
                    primeCnt[curr] += 1
                elif is_prime(curr):
                    """
                    Do NOT judge `is_prime(curr)` each time!

                    If `curr in primeCnt`, then it should be prime!

                    Otherwise, time limit will be exceeded!
                    """
                    primeCnt[curr] = 1
                last = curr
                x += dx
                y += dy

        for x in range(X):
            for y in range(Y):
                for dx in [1, 0, -1]:
                    for dy in [1, 0, -1]:
                        if dx == 0 and dy == 0:
                            continue
                        walk_from(x, y, dx, dy)

        if not primeCnt:
            return -1

        ans, maxCount = 0, 0
        for prime, cnt in primeCnt.items():
            if cnt > maxCount or (cnt == maxCount and prime > ans):
                ans = prime
                maxCount = cnt

        return ans
