def bubble_sort(array):
    for outer in range(len(array) - 1):
        noswap = True
        for inner in range(len(array) - outer - 1):
            if array[inner] > array[inner + 1]:
                array[inner], array[inner + 1] = array[inner + 1], array[inner]
                noswap = False
        if noswap:
            break


def bubble_sort_recur(array):
    if len(array) < 2:
        return array
    else:
        return bubble_sort_outer(array, len(array) - 1)


def bubble_sort_outer(array, end):
    if end < 1:
        return array
    else:
        return bubble_sort_outer(bubble_sort_inner(array, 0, end), end - 1)


def bubble_sort_inner(array, start, end):
    if start >= end:
        return array
    else:
        if array[start] > array[start + 1]:
            array[start], array[start + 1] = array[start + 1], array[start]
        return bubble_sort_inner(array, start + 1, end)
