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