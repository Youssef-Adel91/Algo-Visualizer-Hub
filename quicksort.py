def partition(arr, low, high):
   
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


def quicksort(arr, start, end):
   
    if start < end:
       
        pivot_index = partition(arr, start, end)
        
        quicksort(arr, start, pivot_index - 1)
        
        quicksort(arr, pivot_index + 1, end)

# Test your implementation
mylist = [5, 4, 3, 2, 1]
quicksort(mylist, 0, len(mylist) - 1)
print("unSorted list:", mylist)
print("Expected:    [1, 2, 3, 4, 5]")

# Additional test cases
test1 = [10, 7, 8, 9, 1, 5]
quicksort(test1, 0, len(test1) - 1)
print("\nTest 1:", test1)
print("Expected: [1, 5, 7, 8, 9, 10]")

test2 = [1]
quicksort(test2, 0, len(test2) - 1)
print("\nTest 2:", test2)
print("Expected: [1]")

test3 = []
# The quicksort function handles empty/single-element lists internally 
# if called with valid indices, but for an empty list, len(test3)-1 is -1.
# The external check is necessary here to avoid calling quicksort with start > end.
if test3: 
    quicksort(test3, 0, len(test3) - 1) 
print("\nTest 3:", test3)
print("Expected: []")