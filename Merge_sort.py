from typing import List, Any

def merge_sort(arr: List[Any]) -> List[Any]:
    
    # Base case
    if len(arr) <= 1:
        return arr[:]                     # shallow copy

    # Divide
    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])   # left half
    right_sorted = merge_sort(arr[mid:])  # right half

    # Conquer & merge
    return merge(left_sorted, right_sorted)


def merge(left: List[Any], right: List[Any]) -> List[Any]:
    """
    Stable merge of two already-sorted lists.
    """
    result = []
    i = j = 0

    # Merge while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # <= ensures stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements (at most one of these loops will run)
    result.extend(left[i:])
    result.extend(right[j:])

    return result



tests = [
    [],                                   # empty list
    [1],                                  # single element
    [5, 4, 3, 2, 1],                      # reversed
    [3, 1, 4, 1, 5, 9, 2, 6],              # duplicates and random order
    ["z", "a", "m", "a"],                 # strings (lexicographic order)
]

print("Merge Sort Test Results:\n")
for t in tests:
    original = t.copy()                   # keep a copy to show it's unchanged
    sorted_list = merge_sort(t)
    print(f"original: {original}")
    print(f"sorted:   {sorted_list}")
    print(f"original unchanged? {original == t}\n")