def inplace_quick_sort(arr: [], left, right):
    if left >= right:
        return

    pivot = right

    index = left
    large_index = left
    while index < right:
        if arr[index] < arr[pivot]:
            # swap with next
            arr[index], arr[large_index] = arr[large_index], arr[index]
            large_index += 1

        index += 1

    # swap the pivot
    arr[pivot], arr[large_index] = arr[large_index], arr[pivot]

    inplace_quick_sort(arr, left, large_index-1)
    inplace_quick_sort(arr, large_index+1, right)

if __name__ == '__main__':
    unsorted = [4,3, 4, 5, 12, 2, 54, 0, 2, 2]
    inplace_quick_sort(unsorted, 0, len(unsorted) - 1)
    print(unsorted)
