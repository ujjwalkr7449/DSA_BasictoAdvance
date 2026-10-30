""""1. What is Dynamic Programming?
Dynamic Programming (DP) is an algorithmic technique in which we break a big problem into smaller subproblems and store their results to avoid calculating the same thing again.

In simple words:

DP = Recursion + Storing Previous Results"""


"""2. Why do we need DP?"""
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

print(fib(5))


"""3. Two approaches to Dynamic Programming
A. Memoization (Top-Down DP)
Memoization uses recursion and a dictionary or array to store previously calculated results."""
