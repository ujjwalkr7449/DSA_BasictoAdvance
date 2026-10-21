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