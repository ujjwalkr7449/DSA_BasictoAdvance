student = {
    "name": "Ujjwal",
    "age": 22,
    "course": "Python"
}

print(student)



# Empty dictionary
d = {}

# Dictionary with values
d = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(d)

d = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(d["a"])
print(d["b"])

d = {"a": 10, "b": 20}

print(d.get("a"))
print(d.get("x", 0))

d = {}

d["apple"] = 10
d["banana"] = 20

print(d)
d["apple"] = 50

print(d)

d = {
    "a": 10,
    "b": 20,
    "c": 30
}

del d["a"]

print(d)


d = {"a": 10, "b": 20}

d.pop("a")

print(d)

d = {
    "a": 10,
    "b": 20,
    "c": 30
}

for key in d:
    print(key)
    
for value in d.values():
    print(value)
    
for key, value in d.items():
    print(key, value)
    

d = {"a": 10, "b": 20}

print("a" in d)
print(len(d))

arr = [1, 2, 2, 3, 1, 2]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

arr = [1, 2, 2, 3, 1, 2]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)

freq[num] = freq.get(num, 0) + 1


s = "banana"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

arr = [1, 2, 3, 2, 4, 1]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num, count in freq.items():
    if count > 1:
        print(num)