def FindIndex(mapping, target):
    for i in range(len(mapping)):
        if mapping[i] == target.lower():
            return i
    return -1


def KtoDen(kVal, k):
    denVal = 0
    mapping = "0123456789abcdefghijklmnopqrstuvwxyz"
    for i in range(len(kVal)):
        denVal += FindIndex(mapping, kVal[i] * k ** (len(kVal) - i - 1))
    return denVal


def DentoK(denVal, k):
    mapping = "0123456789abcdefghijklmnopqrstuvwxyz"
    kVal = ""
    while denVal > 0:
        kVal = mapping[denVal % k] + kVal
        denVal //= k

    return kVal


def DentoBinR(denVal):
    if denVal == 0 or denVal == 1:
        print(denVal)
    else:
        mod = denVal % 2
        DentoBinR(denVal // 2)
        print(mod)


def dec2bin(n):
    if n < 0:
        return 'Must be a positive integer'
    elif n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return dec2bin(n // 2) + str(n % 2)
