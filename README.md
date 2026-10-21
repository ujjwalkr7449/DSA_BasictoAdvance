# DSA_BasictoAdvance
# 🐍 Python Basics for DSA

A beginner-friendly guide to learning Python fundamentals for **Data Structures and Algorithms (DSA)**, logical thinking, problem-solving, and coding interview preparation.

The goal is to understand the logic behind every program instead of memorizing solutions.

---

## 📚 Table of Contents

1. [Introduction](#-introduction)
2. [Python Input and Output](#1-python-input-and-output)
3. [Variables and Data Types](#2-variables-and-data-types)
4. [Operators](#3-operators)
5. [Conditional Statements](#4-conditional-statements)
6. [Loops](#5-loops)
7. [Number-Based Programs](#6-number-based-programs)
8. [Pattern Programs](#7-pattern-programs)
9. [String Programs](#8-string-programs)
10. [List and Array Programs](#9-list-and-array-programs)
11. [Dictionary and Set Basics](#10-dictionary-and-set-basics)
12. [Functions](#11-functions)
13. [Searching Basics](#12-searching-basics)
14. [Time Complexity Basics](#13-time-complexity-basics)
15. [Common Python Shortcuts](#14-common-python-shortcuts)
16. [Practice Questions](#15-practice-questions)
17. [DSA Learning Roadmap](#-dsa-learning-roadmap)

---

## 🎯 Introduction

**What is DSA?**

DSA stands for Data Structures and Algorithms.

- **Data Structures:** Ways to store and organize data.
- **Algorithms:** Steps used to solve a problem.

### Why learn Python before DSA?

Python provides simple syntax, built-in data structures, and useful functions that help you focus on problem-solving.

### Basic Problem-Solving Approach

1. Understand the problem.
2. Identify the input and expected output.
3. Think about the logic.
4. Write the algorithm.
5. Convert the logic into Python code.
6. Test with different inputs.
7. Optimize the solution.

---

## 1. Python Input and Output

### Example 1: Print a message

```python
print("Hello, World!")
```

**Output:**
```text
Hello, World!
```

### Example 2: Take input

```python
name = input("Enter your name: ")
print("Hello", name)
```

### Example 3: Take integer input

```python
n = int(input("Enter a number: "))
print(n)
```

### Example 4: Take multiple numbers in a list

```python
arr = list(map(int, input().split()))
print(arr)
```

**Input:**
```text
10 20 30 40
```

**Output:**
```text
[10, 20, 30, 40]
```

**Remember:**

- `input()` reads input as a string.
- `int()` converts a value to an integer.
- `split()` separates input using whitespace by default.
- `map(int, ...)` converts each input value to an integer.
- `list()` stores the converted values in a list.

---

## 2. Variables and Data Types

A variable stores a value.

```python
age = 21
price = 99.5
name = "Ujjwal"
is_student = True

print(age)
print(price)
print(name)
print(is_student)
```

### Common Data Types

| Data Type | Example | Use |
|---|---|---|
| `int` | `10` | Whole numbers |
| `float` | `10.5` | Decimal numbers |
| `str` | `"Python"` | Text |
| `bool` | `True` | True or false |
| `list` | `[1, 2, 3]` | Ordered collection |
| `tuple` | `(1, 2, 3)` | Immutable collection |
| `set` | `{1, 2, 3}` | Unique elements |
| `dict` | `{"age": 21}` | Key-value pairs |

---

## 3. Operators

### Arithmetic Operators

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

### Important Operators for DSA

| Operator | Meaning | Example |
|---|---|---|
| `%` | Remainder | `10 % 3 = 1` |
| `//` | Floor division | `10 // 3 = 3` |
| `==` | Equal to | `5 == 5` |
| `!=` | Not equal to | `5 != 3` |
| `and` | Both conditions true | `a > 0 and b > 0` |
| `or` | At least one condition true | `a > 0 or b > 0` |

**DSA tip:** The modulo operator `%` is frequently used for even/odd checks, digit extraction, and divisibility problems.

---

## 4. Conditional Statements

### Example 1: Even or Odd

```python
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Example 2: Find the Largest of Two Numbers

```python
a = 10
b = 20

if a > b:
    print(a)
else:
    print(b)
```

### Example 3: Positive, Negative, or Zero

```python
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

**Remember:**

- `if` checks a condition.
- `elif` checks another condition.
- `else` runs when the preceding conditions are false.

---

## 5. Loops

Loops execute a block of code repeatedly.

### Example 1: Print Numbers from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

`range(1, 11)` generates numbers from 1 to 10. The ending value is excluded.

### Example 2: Sum of First N Natural Numbers

```python
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print(total)
```

For `n = 5`, the output is `15`.

### Example 3: While Loop

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

### Example 4: Break and Continue

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

`continue` skips the current iteration. `break` stops the loop completely.

---

## 6. Number-Based Programs

### Program 1: Sum of Digits

```python
n = abs(int(input("Enter a number: ")))
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print(total)
```

Example: `1234` → `1 + 2 + 3 + 4 = 10`.

### Program 2: Reverse a Number

```python
n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse)
```

Example: `1234` → `4321`.

### Program 3: Factorial

```python
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)
```

Example: `5! = 5 × 4 × 3 × 2 × 1 = 120`.

Factorial is defined here for non-negative integers.

### Program 4: Palindrome Number

```python
n = int(input("Enter a number: "))
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if original >= 0 and original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
```

Example: `121` is a palindrome.

### Program 5: Prime Number

```python
n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    print("Prime" if is_prime else "Not Prime")
```

A prime number has exactly two positive divisors: 1 and itself.

---

## 7. Pattern Programs

### Pattern 1: Right-Angled Triangle

```python
n = 5

for i in range(1, n + 1):
    print("*" * i)
```

Output:

```text
*
**
***
****
*****
```

### Pattern 2: Number Triangle

```python
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

Output:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

**Logic:** The outer loop controls rows; the inner loop controls what appears in each row.

---

## 8. String Programs

### Program 1: Reverse a String

```python
s = input("Enter a string: ")
print(s[::-1])
```

Example: `"python"` → `"nohtyp"`.

### Program 2: Check String Palindrome

```python
s = input("Enter a string: ").lower()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

This basic version is case-insensitive but does not remove spaces or punctuation.

### Program 3: Count Vowels

```python
s = input("Enter a string: ").lower()
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print(count)
```

### Program 4: Character Frequency

```python
s = "banana"
frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)
```

Output:

```text
{'b': 1, 'a': 3, 'n': 2}
```

**DSA concept:** Dictionaries and frequency counting.

---

## 9. List and Array Programs

Python lists are commonly used to practice array problems.

### Program 1: Sum of List Elements

```python
arr = [10, 20, 30, 40]
total = 0

for num in arr:
    total += num

print(total)
```

Output: `100`.

### Program 2: Find the Largest Element

```python
arr = [12, 45, 7, 89, 23]
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(largest)
```

Output: `89`.

### Program 3: Find the Smallest Element

```python
arr = [12, 45, 7, 89, 23]
smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print(smallest)
```

Output: `7`.

### Program 4: Find the Second-Largest Distinct Element

```python
arr = [10, 25, 8, 25, 18]

largest = float("-inf")
second = float("-inf")

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

if second == float("-inf"):
    print("No second-largest distinct element")
else:
    print(second)
```

Output: `18`.

### Program 5: Reverse a List Using Two Pointers

```python
arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
```

Output:

```text
[5, 4, 3, 2, 1]
```

**DSA concept:** Two pointers.

### Program 6: Remove Duplicates While Preserving Order

```python
arr = [1, 2, 2, 3, 1, 4]
result = []

for num in arr:
    if num not in result:
        result.append(num)

print(result)
```

Output:

```text
[1, 2, 3, 4]
```

This beginner version can take O(n²) time. Later, practice the more efficient set-based approach.

---

## 10. Dictionary and Set Basics

### Dictionary: Count Frequencies

```python
arr = [1, 2, 2, 3, 3, 3]
frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)
```

Output:

```text
{1: 1, 2: 2, 3: 3}
```

### Set: Find Unique Elements

```python
arr = [1, 2, 2, 3, 3, 4]
unique = set(arr)

print(unique)
```

A set stores unique elements. Do not rely on a set to preserve the original list order.

### Check Whether an Element Exists

```python
arr = [10, 20, 30, 40]
target = 30

if target in arr:
    print("Found")
else:
    print("Not Found")
```

---

## 11. Functions

Functions let you reuse logic instead of repeating code.

### Example 1: Add Two Numbers

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

### Example 2: Check Even or Odd

```python
def is_even(n):
    return n % 2 == 0

print(is_even(10))  # True
print(is_even(7))   # False
```

### Example 3: Find the Maximum

```python
def find_max(arr):
    if not arr:
        return None

    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

print(find_max([10, 50, 20, 80, 30]))
```

Output: `80`.

**Remember:**

- `def` defines a function.
- Parameters receive input.
- `return` sends a result back to the caller.

---

## 12. Searching Basics

### Linear Search

Check elements one by one until the target is found.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

arr = [10, 20, 30, 40]
print(linear_search(arr, 30))
```

Output: `2` (the index of `30`).

**Time complexity:** O(n).

### Binary Search

Binary search repeatedly halves the search range. The input list must be sorted.

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 40))
```

Output: `3`.

**Time complexity:** O(log n).

---

## 13. Time Complexity Basics

Time complexity describes how an algorithm's running time grows as input size increases.

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | Access `arr[0]` |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Two nested loops over n elements |

### Example: O(n)

```python
for num in arr:
    print(num)
```

The loop visits each element once.

### Example: O(n²)

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The inner loop runs n times for each of n outer-loop iterations.

**Interview tip:** Learn to explain both the time complexity and the extra space used by your solution.

---

## 14. Common Python Shortcuts

```python
arr = [10, 20, 30, 40, 50]

print(len(arr))       # Number of elements
print(sum(arr))       # Sum
print(max(arr))       # Largest
print(min(arr))       # Smallest
print(arr[0])         # First element
print(arr[-1])        # Last element
print(arr[::-1])      # Reversed copy
print(sorted(arr))    # New sorted list
```

### Useful Input Patterns

```python
# One integer
n = int(input())

# Two integers on one line
a, b = map(int, input().split())

# A list of integers
arr = list(map(int, input().split()))

# A list of strings
words = input().split()
```

**Important:** Learn both built-in functions and manual implementations. In interviews, manual solutions help demonstrate your understanding of the underlying logic.

---

## 15. Practice Questions

Try to solve these questions without looking at the solutions.

### Beginner Level

- [ ] Print numbers from 1 to N.
- [ ] Find the sum of N natural numbers.
- [ ] Check whether a number is even or odd.
- [ ] Find the factorial of a number.
- [ ] Check whether a number is prime.
- [ ] Reverse a number.
- [ ] Calculate the sum of digits.
- [ ] Check whether a number is a palindrome.

### String Level

- [ ] Reverse a string.
- [ ] Count vowels in a string.
- [ ] Check whether a string is a palindrome.
- [ ] Count each character's frequency.
- [ ] Check whether two strings are anagrams.

### Array / List Level

- [ ] Find the largest element.
- [ ] Find the smallest element.
- [ ] Find the second-largest distinct element.
- [ ] Reverse a list without slicing.
- [ ] Count even and odd elements.
- [ ] Remove duplicates.
- [ ] Find the frequency of each element.
- [ ] Search for an element.
- [ ] Move all zeros to the end.
- [ ] Find two numbers that add up to a target.

---

## 🗺️ DSA Learning Roadmap

Follow this order to build your problem-solving skills.

1. **Python fundamentals** — Variables, conditions, loops, functions.
2. **Number and pattern problems** — Strengthen basic logic.
3. **Strings and arrays** — Indexing, traversal, frequency counting.
4. **Hashing** — Dictionaries and sets.
5. **Searching and sorting** — Linear search, binary search, basic sorting.
6. **Two pointers and sliding window** — Solve common array and string problems.
7. **Recursion and backtracking** — Break problems into smaller subproblems.
8. **Linked lists, stacks and queues** — Learn core data structures.
9. **Trees, heaps and graphs** — Learn advanced data structures.
10. **Dynamic programming** — Solve problems involving overlapping subproblems.

---

## 💡 My Revision Strategy

For every problem:

1. Understand the question.
2. Write the logic in simple English.
3. Dry-run the example using pen and paper.
4. Write the Python code.
5. Test edge cases, such as an empty list or a single element.
6. Analyze time and space complexity.
7. Solve the same problem again without checking your notes.

### Golden Rule

**Understand the logic → Write the code → Test it → Optimize it → Explain it.**

Consistent practice is more valuable than memorizing hundreds of programs.

---

## 🛠️ How to Run the Programs

1. Install Python 3.
2. Create a file, for example, `even_odd.py`.
3. Write the program in the file.
4. Open a terminal in the project directory.
5. Run:

```bash
python even_odd.py
```

---

## 🎯 Goal

Build a strong Python foundation, improve logical thinking, and prepare for DSA-based coding interviews.

**Practice every day. Focus on understanding, not memorization.**

Happy Coding! 🚀
