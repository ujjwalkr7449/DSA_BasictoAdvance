#Sum of first N natural numbers

def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)

print(sum_n(5))

#Factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))


#Print numbers from 1 to N
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)

#Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return ""

    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))


#Fibonacci sequence

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i), end=" ")
    
#How recursion actually executes
def calculate(n):
    if n == 0:
        return 0

    return n + calculate(n - 1)

print(calculate(3))
