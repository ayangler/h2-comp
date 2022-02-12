def insertion_sort(array):
    cmp = 0
    for i in range(1, len(array)):
        curr = array[i]
        j = i - 1
        while j >= 0 and curr < array[j]:
            cmp += 1
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = curr
