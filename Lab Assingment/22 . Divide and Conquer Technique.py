#Program to Demonstrate Divide and Conquer Technique (Binary Search)

def binary_search(arr, low, high, key):
   if low <= high:
       mid = (low + high) // 2

       if arr[mid] == key:
           return mid
       elif arr[mid] > key:
           return binary_search(arr, low, mid - 1, key)
       else:
           return binary_search(arr, mid + 1, high, key)

   return -1

# Driver Code
arr = [10, 20, 30, 40, 50, 60, 70]
key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
   print("Element found at index", result)
else:
   print("Element not found")
