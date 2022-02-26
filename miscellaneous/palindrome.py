from math import sqrt


def isPalindrome(n):
    n = str(n)
    while len(n) > 1:
        if n[0] != n[-1]:
            return False
        n = n[1:-1]
    return True


def isSquareOfPalindrome(n):
    for i in range(1, int(sqrt(n)) + 1):
        if isPalindrome(i):
            if i ** 2 == n:
                return True
    return False
