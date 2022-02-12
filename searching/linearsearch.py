def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i

    return -1


def linear_search_recur(array, target, first=0, calls=1):
    if len(array) == 0:
        return (-1, calls)
    elif target == array[0]:
        return (first, calls)
    else:
        return linear_search_recur(array[1:], target, first + 1, calls + 1)


def linear_search_recur2(array, target, start):
    if start > len(array) - 1:
        return -1
    elif target == array[start]:
        return start
    else:
        return linear_search_recur2(array, target, start + 1)
