#Program 1: Sum of first N natural numbers

def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)

print(sum_n(5))

#Program 2: Factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))


#Program 3: Print numbers from 1 to N
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)

#Program 4: Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return ""

    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))