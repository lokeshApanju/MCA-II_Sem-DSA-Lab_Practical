# Program to Compare Sorting Algorithms Based on Execution Time

import time
import random


def selection_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    end = time.time()
    return round((end - start) * 1000, 4) 

print("=== Sorting Algorithm Time Comparison ===")
n = int(input("Enter number of random elements to sort: "))

arr = random.sample(range(1, n * 10), n)
print(f"\nGenerated {n} random elements.")
print("First 10 elements:", arr[:10], "...")

print("\nRunning all sorting algorithms...\n")

t1 = measure_time(selection_sort, arr)
t2 = measure_time(insertion_sort, arr)
t3 = measure_time(merge_sort, arr)

print(f"{'Algorithm':<20} {'Time (ms)':>12}")
print("-" * 34)
print(f"{'Selection Sort':<20} {t1:>12}")
print(f"{'Insertion Sort':<20} {t2:>12}")
print(f"{'Merge Sort':<20} {t3:>12}")

times = {'Selection Sort': t1, 'Insertion Sort': t2, 'Merge Sort': t3}
fastest = min(times, key=times.get)
print(f"\nFastest Algorithm: {fastest}")


