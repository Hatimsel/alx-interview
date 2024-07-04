#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """Returns the winner of the game"""
    def calculate_primes_up_to(n):
        """Calculates all primes possible up to n"""
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False
        primes = [p for p in range(n + 1) if is_prime[p]]
        return primes

    def winner_of_game(n):
        primes = calculate_primes_up_to(n)

        current_set = set(range(1, n + 1))
        maria_turn = True

        while True:
            available_moves = [p for p in primes if p in current_set]

            if not available_moves:
                return "Ben" if maria_turn else "Maria"

            chosen_prime = min(available_moves)
            for multiple in range(chosen_prime, n + 1, chosen_prime):
                if multiple in current_set:
                    current_set.remove(multiple)

            maria_turn = not maria_turn

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = winner_of_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
