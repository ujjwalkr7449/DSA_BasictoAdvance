
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
    
#Example 2: Linear Search Using a Function

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


arr = [5, 10, 15, 20, 25]

print(linear_search(arr, 15))
print(linear_search(arr, 100))


#Example: Binary Search in Python

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70]

print(binary_search(arr, 50))
print(binary_search(arr, 25))

#using sort()

arr = [50, 10, 40, 20, 30]

arr.sort()

print(arr)
 
 
 
#5. Bubble Sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [5, 3, 8, 1, 2]

print(bubble_sort(arr))


#Optimized Bubble Sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


print(bubble_sort([5, 3, 8, 1, 2]))

#6. Selection Sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]

print(selection_sort(arr))

#7. Insertion Sort
