"""1. Advanced Dynamic Programming (Bitmask DP)
Question: Solve the Travelling Salesperson Problem (TSP) using Bitmask DP to find the minimum cost to visit all cities and return to the start."""
#but need to some programe for for this topics
"""1. Recursion
Problem: Find the factorial of a number using recursion.

Approach:

Base Case: Define the stopping condition (if n == 0 or n == 1, return 1) to prevent infinite recursion and stack overflow.

Recursive Step: Break the problem down into a smaller subproblem: n * factorial(n - 1).

Call Stack: The program pushes function calls onto the call stack until it hits the base case, then resolves values as it unwinds."""
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive step
  return n * factorial(n - 1)


# Example usage:
print("Factorial of 5:", factorial(5))  

"""2. Bit Manipulation
Problem: Check whether a number is even or odd using bitwise operators.

Approach:

Look at the least significant bit (LSB) of a binary number.

For any even number, the LSB is always 0. For any odd number, the LSB is always 1.

Use the bitwise AND operator (n & 1) to mask out all other bits and check if the result is 0 or 1."""
def is_even(n):
  # If n & 1 is 0, the last bit is 0 (even)
  return (n & 1) == 0


# Example usage:
print("Is 4 even?", is_even(4))  # Output: True
print("Is 7 even?", is_even(7))  # Output: False

"""3. Sorting & Custom Comparators
Problem: Sort a list of intervals based on their ending times.

Approach:

Use Python's built-in Timsort algorithm (sorted()).

Pass a custom key using a lambda function to tell Python to 
sort based on a specific element inside the tuples 
(e.g., index 1 for the end time), which is a core technique in Greedy algorithms."""

def sort_intervals(intervals):
  # intervals = [[start, end], ...]
  # Sort by the end time (index 1)
  return sorted(intervals, key=lambda x: x[1])


# Example usage:
intervals = [[1, 3], [2, 4], [0, 6], [5, 7]]
print("Sorted intervals by end time:", sort_intervals(intervals))
# Output: [[1, 3], [2, 4], [0, 6], [5, 7]]

"""4. Two Pointers PatternProblem: 
Check if a string is a valid palindrome
(reads the same forward and backward).Approach:Initialize two pointers: left at the start index (0)
and right at the end index (len(s) - 1).Compare characters at both pointers. If they don't match, 
it's not a palindrome.Move left forward and right backward towards the center until they meet, 
reducing time complexity to $O(n)$ and space to $O(1)$."""
def is_palindrome(s):
  left, right = 0, len(s) - 1

  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True


# Example usage:
print("Is 'racecar' a palindrome?", is_palindrome("racecar"))  # Output: True
print("Is 'hello' a palindrome?", is_palindrome("hello"))  # Output: False