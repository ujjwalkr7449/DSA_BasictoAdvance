numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
    
numbers = [10, 20, 30, 40]

total = 0
for num in numbers:
    total += num

print(total)



numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)

#Find the smallest element
numbers = [12, 45, 7, 89, 23]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

#Reverse a list without reverse()
numbers = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)