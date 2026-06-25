# Program to Implement Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"  Pass {i+1}: {arr}")

    return arr

print("=== Selection Sort ===")
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"  Element {i+1}: ")))

print("\nOriginal Array:", arr)
print("\nSorting Step by Step:")

sorted_arr = selection_sort(arr)

print("\nSorted Array:", sorted_arr)
