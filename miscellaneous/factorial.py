def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


def iterativeFactorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
