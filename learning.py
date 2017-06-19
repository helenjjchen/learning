
def factorial(n):
    if type(n) is not int >= 1:
        return "error"
    elif n == 1:
        return n
    else:
        return n*factorial(n-1)

n = 7
print factorial(n)

n = "hello"
print factorial(n)

n = 6.8
print factorial(n)