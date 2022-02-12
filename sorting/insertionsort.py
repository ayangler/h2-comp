def insertion_sort(array):
    cmp, swp = 0, 0
    for i in range(len(array)):
        for j in range(i, 0, -1):
            cmp += 1
            if array[j] < array[j - 1]:
                swp += 1
                array[j], array[j - 1] = array[j - 1], array[j]
