#!/usr/bin/python3
"""Change comes from within"""
from collections import deque


def makeChange(coins, total):
    if total <= 0:
        return 0

    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        current_amount, coin_count = queue.popleft()

        for coin in coins:
            new_amount = current_amount + coin

            if new_amount == total:
                return coin_count + 1
            if new_amount < total and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, coin_count + 1))

    return -1
