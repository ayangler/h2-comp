def binary_search(a, t):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if t == a[mid]:
            return True
        elif t < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


def binary_search_repeated(aList, target):  # with repeated items, returns all instances
    n = len(aList)
    low = 0
    high = n - 1
    found = False
    index = []

    while not found and low <= high:
        mid = (low + high) // 2

        if aList[mid] == target:
            found = True
            index = [mid]

            # search left
            left = mid - 1
            while left >= 0 and aList[left] == target:
                index.append(left)
                left -= 1

            # search right
            right = mid + 1
            while right < n and aList[right] == target:
                index.append(right)
                right += 1

        elif aList[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    if found:
        index.sort()
        return index
    else:
        return -1


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 1, 1, 2, 2, 3, 3]
    print("binary_search", binary_search_repeated(list1, 1))
    print("binary_search", binary_search_repeated(list1, 0))
    print("binary_search_repeated", binary_search_repeated(list2, 1))
    print("binary_search_repeated", binary_search_repeated(list2, 0))
