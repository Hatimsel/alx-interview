#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """Returns the winner of a prime game"""
    def sieve(n):
        """REturns all possible prime numbers up to n"""
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0] = is_prime[1] = False
        primes = [i for i in range(n + 1) if is_prime[i]]
        return primes, is_prime

    def count_primes_up_to(n, primes, is_prime):
        """Counts prime numbers up to n"""
        if n < 2:
            return 0
        return sum(is_prime[2:n+1])

    max_n = max(nums)
    primes, is_prime = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n, primes, is_prime)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
