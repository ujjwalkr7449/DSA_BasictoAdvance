
arr = [10, 20, 30, 40, 50]

target = 30

if target in arr:
    print("Element found")
else:
    print("Element not found")

#Example 1: Basic Linear Search

arr = [10, 20, 30, 40, 50]

target = 40

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index:", i)
        break
