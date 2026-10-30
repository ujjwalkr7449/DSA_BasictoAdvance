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

def fib(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib(n-1, dp) + fib(n-2, dp)

    return dp[n]


n = 6
dp = [-1] * (n + 1)

print(fib(n, dp))

"""B. Tabulation (Bottom-Up DP)
Tabulation uses iteration instead of recursion."""
def fib(n):
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


print(fib(6))

"""Problem 1: Fibonacci Number
Given a number n, find the nth Fibonacci number using Dynamic Programming."""
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(fib(7))
#Problem 2: Climbing Stairs
#You can climb either 1 or 2 steps at a time. Find the number of ways to reach the nth stair.
def climbStairs(n):
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(climbStairs(4))

"""Problem 3: House Robber
You cannot rob two adjacent houses. Find the maximum money you can rob."""
def rob(nums):
    prev2 = 0
    prev1 = 0

    for money in nums:
        curr = max(prev1, prev2 + money)

        prev2 = prev1
        prev1 = curr

    return prev1

print(rob([2, 7, 9, 3, 1]))

"""Problem 4: Minimum Cost Climbing Stairs"""
def minCostClimbingStairs(cost):
    prev2 = 0
    prev1 = 0

    for i in range(2, len(cost) + 1):
        curr = min(
            prev1 + cost[i-1],
            prev2 + cost[i-2]
        )

        prev2 = prev1
        prev1 = curr

    return prev1

print(minCostClimbingStairs([10, 15, 20]))
