def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


print(Factorial(0))


def iterativeFactorial(n):
    if n == 0:
        return 1
    else:
        res = 1
        while n != 1:
            res *= n
            n -= 1

    return res
