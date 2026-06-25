# Program to Implement Binary Search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        mid = (low + high) // 2
        steps += 1
        print(f"  Step {steps}: Checking index {mid}, value = {arr[mid]}")

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps

print("=== Binary Search ===")
print("Note: Array must be sorted for binary search.")

n = int(input("Enter number of elements: "))
arr = []
print("Enter elements in sorted (ascending) order:")
for i in range(n):
    arr.append(int(input(f"  Element {i+1}: ")))

arr.sort()  # Ensure sorted
print("\nSorted Array:", arr)

target = int(input("Enter element to search: "))

print("\nSearching...")
index, steps = binary_search(arr, target)

if index != -1:
    print(f"\nElement {target} found at index {index} in {steps} step(s).")
else:
    print(f"\nElement {target} not found. Steps taken: {steps}.")

