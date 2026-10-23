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


#Count even and odd numbers
numbers = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)

#Remove duplicates
numbers = [1, 2, 2, 3, 3, 4]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

#Find the second-largest distinct element
numbers = [10, 5, 20, 8, 20]

unique = sorted(set(numbers))

if len(unique) >= 2:
    print(unique[-2])
else:
    print("No second-largest element")
    
    
    
#Tuples 
values = (10, 20, 30, 40)

print(values[0])
print(values[-1])


values = (10, 20, 30, 40, 50)
print(len(values))


values = (10, 20, 30, 40)

print("Sum:", sum(values))
print("Maximum:", max(values))

#Count occurrences of an element in a tuple
values = (1, 2, 2, 3, 2, 4)

print(values.count(2))

values = (10, 20, 30, 40)

print(values.index(30))

#Convert a tuple into a list and update it
values = (10, 20, 30)

temp = list(values)
temp[1] = 99
values = tuple(temp)

print(values)


#7. Unpack a tuple
student = ("Ujjwal", 21, "Python")

name, age, skill = student

print(name)
print(age)
print(skill)


#Stringss

text = "python"
print(text[::-1])


#2. Check palindrome

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
    

#Count vowels and consonants
text = "python"
vowels = 0
consonants = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


#4. Count character frequency
text = "banana"

for ch in sorted(set(text)):
    print(ch, text.count(ch))
    
    
#5. Check anagrams
a = "listen"
b = "silent"

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not anagram")
    

    
    
sentence = "Python is easy to learn"

words = sentence.split()
print(len(words))


#8. Find the first non-repeating character
text = "aabbcde"

for ch in text:
    if text.count(ch) == 1:
        print(ch)
        break
    
li=[]   
a=int(input("Enter a number: "))
for i in range(a):
    b=int(input("Enter a number: "))
    li.append(b)

    