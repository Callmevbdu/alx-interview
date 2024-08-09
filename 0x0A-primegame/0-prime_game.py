#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including n, they take turns choosing a prime number from the
set and removing that number and its multiples from the set. The player that
cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally, determine who
the winner of each game is.
"""


def isWinner(x, nums):
    """
    * Prototype: def isWinner(x, nums)
    * where x is the number of rounds and nums is an array of n
    * Return: name of the player that won the most rounds
    * If the winner cannot be determined, return None
    * You can assume n and x will not be larger than 10000
    * You cannot import any packages in this task
    - Example:
    * x = 3, nums = [4, 5, 1]
    - First round: 4
    * Maria picks 2 and removes 2, 4, leaving 1, 3
    * Ben picks 3 and removes 3, leaving 1
    * Ben wins because there are no prime numbers left for Maria to choose
    - Second round: 5
    * Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    * Ben picks 3 and removes 3, leaving 1, 5
    * Maria picks 5 and removes 5, leaving 1
    * Maria wins because there are no prime numbers left for Ben to choose
    - Third round: 1
    * Ben wins because there are no prime numbers for Maria to choose
    - Result: Ben has the most wins
    """
    def is_prime(num):
        """ is_prime function """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """ get_primes function """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_game(n):
        """ play_game function """
        primes = get_primes(n)
        total_rounds = len(primes)
        if total_rounds % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = [play_game(num) for num in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
