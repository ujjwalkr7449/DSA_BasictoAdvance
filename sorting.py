arr = [5, 2, 8, 1, 9, 3]

# Ascending order
[1, 2, 3, 5, 8, 9]

# Descending order
[9, 8, 5, 3, 2, 1]

"""Comparison-based sorting
Beginner
- Bubble Sort
- Selection Sort
- Insertion Sort

Important
- Merge Sort
- Quick Sort
- Heap Sort



Non-comparison-based sorting
- Counting Sort
- Radix Sort
- Bucket Sort"""

"""2. Bubble Sort
Bubble Sort repeatedly compares two adjacent elements and swaps them if they are in the wrong order."""
arr = [5, 3, 8, 4, 2]

n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):

        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

"""3. Selection Sort
Selection Sort finds the smallest element and puts it in the correct position."""

arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):

    min_index = i

    for j in range(i+1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)


"""4. Insertion Sort
Insertion Sort takes one element at a time and inserts it into its correct position in the sorted portion."""
arr = [5, 3, 4, 1, 2]

for i in range(1, len(arr)):

    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:

        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key

print(arr)