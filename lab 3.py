def numbers(n: int):
    print(n)

    if n == 0:
        return
    numbers(n - 1)

print("Zadanie 1")
numbers(20)

def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print("\nZadanie 2")
print(fib(7))

def power(number: int, n: int) -> int:
    if n < 2:
        return number
    return power(number, n - 1) * power(number, n - 2)

print("\nZadanie 3")
print(power(4, 3))

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("\nZadanie 5")
print(factorial(5))

def prime(n: int) -> bool:
    if n == 1:
        return True

    elif n % 2 == 0:
        return False

    elif n % 3 == 0:
        return False

    elif n % 4 == 0:
        return False

    elif n % 5 == 0:
        return False

    else:
        return True

print("\nZadanie 6")
print(prime(17))