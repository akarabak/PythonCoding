def print_missing(array, total_nums):
    i = 1
    j = 0
    while i < total_nums or j < len(array):
        if j >= len(array):
            print(i)
            i += 1
        elif array[j] != i:
            print(i)
            i += 1
        else:
            j += 1
            i += 1


def pair_that_sums_to_num(array, num):
    complement = set()
    result = []
    for i in array:
        if num - i in complement:
            result.append((num - i, i))
        complement.add(i)

    return result


def pair_that_sums_to_num_sort(array, num):
    array.sort()
    i = 0
    j = len(array) - 1
    result = []
    while i < j:
        first, second = array[i], array[j]
        if first + second == num:
            result.append((first, second))
            i += 1
            j -= 1
        elif first + second > num:
            j -= 1
        else:
            i += 1
    return result
