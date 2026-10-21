print("Hello, World!")

name = input("Enter your name: ")
print("Hello", name)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)


n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
    
for i in range(1, 11):
    print(i)
    
    
    
    
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
    
    n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)


n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse)



n = int(input("Enter a number: "))
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if original == reverse:
    print("Palindrome")
else:

    print("Not palindrome")
    
    
    
n = abs(int(input("Enter a number: ")))
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10

print("Digits:", count)



s = input("Enter a string: ")
print(s[::-1])

s = input("Enter a string: ").lower()
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print("Vowels:", count)