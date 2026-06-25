# Program to Implement Insertion Sort

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"  Pass {i}: {arr}  (inserted {key})")

    return arr

print("=== Insertion Sort ===")
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"  Element {i+1}: ")))

print("\nOriginal Array:", arr)
print("\nSorting Step by Step:")

sorted_arr = insertion_sort(arr)

print("\nSorted Array:", sorted_arr)
